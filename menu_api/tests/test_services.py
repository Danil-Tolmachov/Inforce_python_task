import pytest
from core_app import services
from core_app.models import Restaurant, Menu
from auth_app.models import Employee


@pytest.mark.django_db
def test_get_choosen_menus(authenticated_client, url):
    restaurant_1 = Restaurant.objects.create(
        name='test1',
        address='test_address1'
    )

    restaurant_2 = Restaurant.objects.create(
        name='test2',
        address='test_address2'
    )

    menu_1 = Menu.objects.create(
        items={
            'Product1': 500,
            'Product2': 250
        }
    )

    menu_2 = Menu.objects.create(
        items={
            'Product3': 600,
            'Product4': 150
        }
    )

    restaurant_1.menu = menu_1
    restaurant_2.menu = menu_2
    restaurant_1.save()
    restaurant_2.save()

    menu_1.votes.add(Employee.objects.first())

    assert services.get_choosen_menu() == menu_1
