import pytest


@pytest.mark.django_db
def test_gettodaysmenu_view(authenticated_client, url):
    response = authenticated_client.get(url('menu'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_createrestaurant_view(authenticated_client, url):

    data = {
        'name': 'test',
        'address': 'test_address'
    }

    response = authenticated_client.post(url('create-restaurant'), data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_uploadrestaurantmenu_view(authenticated_client, url, restaurant):
    restaurant.save()

    data = {
        'items': {
         "Pizza": 600,
         "ss": 100
        }
    }

    response = authenticated_client.post(
        url('update-menu') + f'?restaurant={restaurant.pk}',
        data,
        format='json'
    )
    assert response.status_code == 201
