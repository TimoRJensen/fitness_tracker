import datetime

import pytest
from django.contrib.auth import get_user_model
from tracker.models import Measurement

User = get_user_model()


@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(
        username="testuser", password="testpass123", email="testuser@example.com"
    )
    assert user.username == "testuser"
    assert user.email == "testuser@example.com"
    assert user.check_password("testpass123")


@pytest.mark.django_db
def test_measurement_creation():
    user = User.objects.create_user(username="testuser", password="testpass123")
    measurement = Measurement.objects.create(
        user=user,
        date=datetime.date(2023, 10, 5),
        weight=70.5,
        body_fat_percentage=20.0,
    )
    assert measurement.user == user
    assert measurement.weight == 70.5
    assert measurement.body_fat_percentage == 20.0
    assert str(measurement) == f"Measurement of {user.username} on 2023-10-05"
