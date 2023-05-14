from django.utils import timezone
from django.db import models

from .utils import is_voting_ended
from core_app.exceptions import VotingIsEndedException


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    menu = models.OneToOneField('core_app.Menu', null=True, default=None, on_delete=models.CASCADE)

    def update_menu(self, restaurant, items):
        Menu.objects.create(items=items, restarant=restaurant)


class Menu(models.Model):
    items = models.JSONField()
    date = models.DateField(default=timezone.now)

    votes = models.ManyToManyField('auth_app.Employee')

    def vote(self, user):

        if not is_voting_ended():
            self.votes.add(user)
            return True

        raise VotingIsEndedException()

    def get_votes_count(self):
        return self.votes.count()
