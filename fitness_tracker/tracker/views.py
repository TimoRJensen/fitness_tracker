from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import MeasurementForm, WorkoutSessionForm
from .models import Measurement, WorkoutSession


@login_required
def add_measurement(request):
    if request.method == "POST":
        form = MeasurementForm(request.POST)
        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.user = request.user
            measurement.save()
            return redirect("index")
    else:
        form = MeasurementForm()
    return render(request, "tracker/add_measurement.html", {"form": form})


@login_required
def add_workout_session(request):
    if request.method == "POST":
        form = WorkoutSessionForm(request.POST)
        if form.is_valid():
            session: WorkoutSession = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect("index")
    else:
        form = WorkoutSessionForm()
    return render(request, "tracker/add_workout_session.html", {"form": form})


@login_required
def index(request):
    measurements = Measurement.objects.filter(user=request.user).order_by("-date")
    workout_sessions = WorkoutSession.objects.filter(user=request.user).order_by(
        "-date"
    )
    return render(
        request,
        "tracker/index.html",
        {"measurements": measurements, "workout_sessions": workout_sessions},
    )
