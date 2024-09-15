from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_measurement/", views.add_measurement, name="add_measurement"),
    path("accounts/", include("django.contrib.auth.urls")),
]
