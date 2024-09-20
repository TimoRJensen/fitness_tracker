from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_measurement/", views.add_measurement, name="add_measurement"),
    path("add_workout_session/", views.add_workout_session, name="add_workout_session"),
    path("accounts/", include("django.contrib.auth.urls")),
]
