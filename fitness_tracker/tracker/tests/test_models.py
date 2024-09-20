import datetime

import pytest
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from tracker.models import Measurement, WorkoutSession

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


User = get_user_model()


@pytest.mark.django_db
def test_workout_session_creation():
    user = User.objects.create_user(username="testuser", password="testpass123")
    workout_date = datetime.date(2023, 10, 10)
    duration = 60  # in Minutes
    notes = "Morning cardio session"

    session: WorkoutSession = WorkoutSession.objects.create(
        user=user, date=workout_date, duration=duration, notes=notes
    )

    assert session.user == user
    assert session.date == workout_date
    assert session.duration == duration
    assert session.notes == notes
    assert str(session) == f"Workout Session of {user.username} on {workout_date}"


@pytest.mark.django_db
def test_workout_session_negative_duration():
    user = User.objects.create_user(username="testuser", password="testpass123")
    workout_date = datetime.date(2023, 10, 10)
    invalid_duration = -30  # Ungültige Dauer (negativ)

    session: WorkoutSession = WorkoutSession(
        user=user,
        date=workout_date,
        duration=invalid_duration,
    )
    # Versuche, die Sitzung zu speichern und erwarte einen ValidationError
    with pytest.raises(ValidationError) as exc_info:
        session.full_clean()  # Validierung auslösen
        session.save()

    assert "duration" in exc_info.value.message_dict
