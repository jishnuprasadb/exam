from django import forms
from django.contrib.auth.forms import UserCreationForm

from exam_app.models import Login, User, Exam


class LoginRegister(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2')

class UserRegister(forms.ModelForm):
    class Meta:
        model=User
        fields = ('name', 'email', 'phone_number', 'address')
class Add_Exam(forms.ModelForm):
    class Meta:
        model=Exam
        fields=('exam_type',)