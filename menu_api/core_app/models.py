from django.utils import timezone
from django.db import models



class Restaurant():
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    username = models.CharField(max_length=70)
    password_hash = models.CharField(max_length=255)


class Menu():
    items = models.JSONField()
    day = models.DateField(default=timezone.now())
    restaurant = models.ForeignKey('core.Restaurant', on_delete=models.SET_NULL)

    votes = models.ManyToManyField('auth.Employee')
