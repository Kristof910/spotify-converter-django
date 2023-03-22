from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("authentication/", views.authenticaiton, name="authentication"),
    path("converter/", views.converter, name="converter"),
    path("end/", views.end, name="end"),
]
