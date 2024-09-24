from django import forms

from .models import Measurement, WorkoutSession


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ["date", "weight", "body_fat_percentage"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "body_fat_percentage": forms.NumberInput(
                attrs={"min": "0", "max": "100", "step": "0.1"}
            ),
        }


class WorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ["date", "duration", "notes"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
