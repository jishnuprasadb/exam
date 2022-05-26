from django.contrib import admin

# Register your models here.
from exam_app.models import User, Exam

admin.site.register(User)
admin.site.register(Exam)