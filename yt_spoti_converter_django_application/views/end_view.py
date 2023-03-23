from django.shortcuts import render


def end(request):
    return render(request, "end.html")
