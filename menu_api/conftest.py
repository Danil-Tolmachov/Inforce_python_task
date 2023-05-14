import json
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from auth_app.models import Employee
from core_app.models import Restaurant


@pytest.fixture
def authenticated_client():
    client = APIClient()
    user = Employee.objects.create_user(
        username='testuser',
        email='testuser@example.com',
        password='testpassword'
    )
    url = reverse('login')
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    response = client.post(url, data, format='json')
    token = json.loads(response.content)['access']
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    return client


@pytest.fixture(scope='session')
def restaurant():
    restaurant = Restaurant(
        name='test',
        address='test_address'
    )
    return restaurant


@pytest.fixture(scope='session')
def url():
    return reverse
