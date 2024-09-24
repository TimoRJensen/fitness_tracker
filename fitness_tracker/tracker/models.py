from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ValidationError


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

    def clean(self) -> None:
        super().clean()
        if self.weight is not None and self.weight <= 0:
            raise ValidationError({"weight": "Weight must be a positive number."})
        if self.body_fat_percentage is not None:
            if not (0 <= self.body_fat_percentage <= 100):
                raise ValidationError(
                    {
                        "body_fat_percentage": (
                            "Body fat percentage must be between 0 " + "and 100."
                        )
                    }
                )

    def __str__(self):
        return f"Measurement of {self.user.username} on {self.date}"


class WorkoutSession(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="workout_sessions"
    )
    date = models.DateField()
    duration = models.PositiveIntegerField()  # Dauer in Minuten
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Workout Session of {self.user.username} on {self.date}"
