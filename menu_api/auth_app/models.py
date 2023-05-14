from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    first_name = models.CharField(max_length=70, null=True)
    last_name = models.CharField(max_length=70, null=True)
    email = models.CharField(max_length=255)

    username = models.CharField(max_length=255, unique=True)

    groups = []
    user_permissions = []
