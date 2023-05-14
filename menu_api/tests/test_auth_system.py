from auth_app.models import Employee

import pytest


@pytest.mark.django_db
def test_login(client, url):
    user = Employee.objects.create_user(
        username='testuser',
        password='testpassword',
        email='testuser@example.com'
    )

    data = {
        'username': 'testuser',
        'password': 'testpassword',
    }

    response = client.post(url('login'), data)

    assert response.status_code == 200


@pytest.mark.django_db
def test_register(client, url):
    data = {
        'username': 'testuser',
        'password': 'testpassword',
        'email': 'test@email.com'
    }

    response = client.post(url('register'), data)
    assert response.status_code == 201

    response = client.post(url('login'), data)
    assert response.status_code == 200
