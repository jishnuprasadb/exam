from django.urls import path

from exam_app import views

urlpatterns=[
    path("",views.home,name='home'),
    path('user_home/',views.user_home,name='user_home'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('login_view/',views.login_view,name='login_view'),
    path('user_registration/',views.user_registration,name='user_registration'),
    path('add_exam/',views.add_exam,name='add_exam'),
    path('exam_view/',views.exam_view,name='exam_view'),
    path('start_exam/',views.start_exam,name='start_exam')
]