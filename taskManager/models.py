from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    user = models.ForeignKey(User,max_length=10, on_delete=models.CASCADE, null=True)

class Profile(models.Model):
    profile_pic = models.ImageField(null=True, blank=True, default='default.jpg')

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
