from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20,null=True,blank=True)