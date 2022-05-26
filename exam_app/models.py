from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user=models.BooleanField(null=True)
class User(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='user')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.TextField()
class Exam(models.Model):
    exam_type=models.CharField(max_length=50)

