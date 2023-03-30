from django.shortcuts import render
from ..converter.converting_manager import converting_manager


def end(request):
    converting_manager(request)

    return render(request, "end.html")
