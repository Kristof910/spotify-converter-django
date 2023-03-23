from django.shortcuts import render
from django.shortcuts import redirect
from ..converter import saving_tokens


def converter(request):

    try:
        saving_tokens.saving_tokens(request)
        
        # POST method
        if request.method == "POST":
            return redirect("end")
        
        # GET method
        return render(request, "converter.html")

    except Exception as e:
        print(f"Ops, something gone wrong in converter: {e}")
        return render(request, "error.html")