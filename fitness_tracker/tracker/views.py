from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import MeasurementForm
from .models import Measurement


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
def index(request):
    measurements = Measurement.objects.filter(user=request.user).order_by("-date")
    return render(request, "tracker/index.html", {"measurements": measurements})
