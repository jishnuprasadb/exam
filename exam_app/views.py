from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
from exam_app.forms import LoginRegister, UserRegister, Add_Exam
from exam_app.models import Exam


def home(request):
    return render(request,'home.html')
def user_home(request):
    return render(request,'user_home.html')
def admin_home(request):
    return render(request,'admin_home.html')
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_user:
                return redirect('user_home')
        else:
            messages.info(request,'invalid credentiels')
    return render(request,'login.html')

def user_registration(request):
    login_form = LoginRegister()
    user_form = UserRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        user_form = UserRegister(request.POST)
        if login_form.is_valid and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            u = user_form.save(commit=False)
            u.user = user
            u.save()
            messages.info(request, 'user register successful')
            return redirect('login_view')
    return render(request, 'user_register.html', {'login_form': login_form, 'user_form': user_form})

def add_exam(request):
    form = Add_Exam()
    if request.method == 'POST':
        form = Add_Exam(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_exam')
    return render(request, 'add_exam.html', {'form': form})

def exam_view(request):
    dataset = Exam.objects.all()
    print(dataset)
    context = {
        'data': dataset
    }
    return render(request, 'select_exam.html', context)

def start_exam(request):
    return render(request,'exam.html')

