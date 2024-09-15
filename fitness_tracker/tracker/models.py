from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Measurement(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="measurements"
    )
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    body_fat_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return f"Measurement of {self.user.username} on {self.date}"
