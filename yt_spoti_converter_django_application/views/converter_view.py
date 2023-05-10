from django.shortcuts import render
from django.shortcuts import redirect
from ..converter.saving_tokens import saving_tokens
import pdb


def converter(request):
    saving_tokens(request)

    if request.method == "POST":
        return redirect("end")

    elif request.method == "GET":
        return render(request, "converter.html")
