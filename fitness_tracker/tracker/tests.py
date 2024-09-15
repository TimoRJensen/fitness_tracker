# tracker/tests/test_models.py

import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(
        username="testuser", password="testpass123", email="testuser@example.com"
    )
    assert user.username == "testuser"
    assert user.email == "testuser@example.com"
    assert user.check_password("testpass123")
