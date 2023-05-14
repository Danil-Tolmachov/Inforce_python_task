from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.CharField(max_length=255)

    username = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    
    groups = []
    user_permissions = []

