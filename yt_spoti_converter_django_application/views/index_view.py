from django.shortcuts import render
from ..utils.enviroment_checker import enviroment_checker


def index(request):
    enviroment_checker()
    return render(request, "index.html")
