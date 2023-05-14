from django.db.models import Count
from django.db.models import QuerySet
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from core_app.models import Menu, Restaurant


def get_choosen_menu() -> QuerySet[Menu]:
    """
        This function returns the menu with the most votes for today, or None if there are no menus with votes.

        Returns:
        - A QuerySet of Menu objects.
    """
    annotated = get_todays_menus().annotate(votes_count=Count('votes'))
    return annotated.order_by('-votes_count').first()


def get_todays_menus() -> QuerySet[Menu]:
    """
        This function returns all menus for today's date.

        Returns:
        - A QuerySet of Menu objects.
    """
    return Menu.objects.filter(date=date.today())


def update_menu(restaurant_id, data) -> bool:
    """
    This function creates the new menu, and changes current menu of the given restaurant with a new one.

    Returns:
        - True is a menu is created successfuly, otherwise False.
    """

    try:
        Restaurant.objects.get(pk=restaurant_id)
    except ObjectDoesNotExist:
        return False

    new_menu = Menu.objects.create(**data)

    obj = Restaurant.objects.get(pk=restaurant_id)
    obj.menu = new_menu
    obj.save()
    return True
