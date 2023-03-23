from django.shortcuts import render
from ..utils import enviroment_checker

def index(request):
    try:
        enviroment_checker.enviroment_checker()
        return render(request, "index.html")

    except Exception as e:
        print(f"Ops, something gone wrong in index: {e}")
        return render(request, "error.html")
