from django.shortcuts import render
from django.shortcuts import redirect
from ..converter.saving_tokens import saving_tokens
import pdb

def converter(request):
    print("CONV STEP ONE")
    try:
        saving_tokens(request)
        
        # POST method
        if request.method == "POST":
            print("CONV STEP THREE")
            # pdb.set_trace()
            # print("ELOOOOOOO")
            return redirect("end")
        
        # GET method
        print("CONV STEP TWO")
        return render(request, "converter.html")

    except Exception as e:
        print(f"Ops, something gone wrong in converter: {e}")
        return render(request, "error.html")