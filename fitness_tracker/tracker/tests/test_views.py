# tracker/tests/test_views.py

import pytest
from django.contrib.auth import get_user_model
from django.test.client import Client
from django.urls import reverse
from tracker.models import Measurement

User = get_user_model()


@pytest.mark.django_db
def test_add_measurement_view_authenticated(client: Client):
    user = User.objects.create_user(username="testuser", password="testpass123")
    client.force_login(user)
    url = reverse("add_measurement")
    response = client.get(url)
    assert response.status_code == 200
    assert b"Add Measurement" in response.content

    # Test the form submission
    response = client.post(
        url, {"date": "2023-10-05", "weight": 70.5, "body_fat_percentage": 20.0}
    )
    assert response.status_code == 302  # Redirect after successful submission
    measurement = Measurement.objects.get(user=user, date="2023-10-05")
    assert measurement.weight == 70.5
    assert measurement.body_fat_percentage == 20.0


def test_add_measurement_view_unauthenticated(client):
    url = reverse("add_measurement")
    response = client.get(url)
    assert response.status_code == 302  # Redirect to login
    assert "/login/" in response.url


@pytest.mark.django_db
def test_user_can_login(client: Client):
    # Erstelle einen Testbenutzer
    username = "testuser"
    password = "testpass123"
    User.objects.create_user(username=username, password=password)

    # Sende eine POST-Anfrage an die Login-URL mit den Anmeldedaten
    url = reverse("login")
    response = client.post(
        url,
        {
            "username": username,
            "password": password,
        },
    )

    # Überprüfe, ob der Benutzer nach erfolgreicher Anmeldung weitergeleitet wird
    assert response.status_code == 302
    assert response.url == reverse("index")

    # Überprüfe, ob der Benutzer tatsächlich angemeldet ist
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert response.wsgi_request.user.is_authenticated
    assert response.wsgi_request.user.username == username


@pytest.mark.django_db
def test_user_can_logout(client: Client):
    username = "testuser"
    password = "testpass123"
    user = User.objects.create_user(username=username, password=password)
    client.force_login(user)

    url = reverse("logout")
    response = client.post(url)

    assert response.status_code == 302
    assert response.url == reverse("login")

    assert "_auth_user_id" not in client.session


def test_login_required_redirect(client: Client):
    url = reverse("add_measurement")
    response = client.get(url)
    assert response.status_code == 302
    assert "/accounts/login/" in response.url
