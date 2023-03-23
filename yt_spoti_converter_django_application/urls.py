from django.urls import path
from .views import index_view, authentication_view, converter_view, end_view

urlpatterns = [
    path("", index_view.index, name="index"),
    path("authentication/", authentication_view.authenticaiton, name="authentication"),
    path("converter/", converter_view.converter, name="converter"),
    path("end/", end_view.end, name="end"),
]
