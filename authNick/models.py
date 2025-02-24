from django.contrib.auth.models import AbstractUser
from django.db import models
from polls.models import Question

class Users(AbstractUser):  # ✅ ПРАВИЛЬНО
    current_question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True)
