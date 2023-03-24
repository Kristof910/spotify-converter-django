from django.urls import path
from .views.index_view import index
from .views.authentication_view import authenticaiton
from .views.converter_view import converter
from .views.end_view import end

urlpatterns = [
    path("", index, name="index"),
    path("authentication/", authenticaiton, name="authentication"),
    path("converter/", converter, name="converter"),
    path("end/", end, name="end"),
]
