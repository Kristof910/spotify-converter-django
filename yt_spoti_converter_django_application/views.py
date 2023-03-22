from django.shortcuts import render
import os
from django.shortcuts import redirect


def index(request):
    try:
        # print("FOR DEBUG: ", os.environ.get("SPOTI_CLIENT_ID"))
        if (
            os.environ.get("SPOTI_CLIENT_ID") == None
            or os.environ.get("SPOTI_CLIENT_SECRET") == None
            or os.environ.get("YT_API_KEY") == None
            or os.environ.get("DOMAIN_OR_IP") == None
        ):
            raise Exception("Enviroment variables not set!")

        return render(request, "index.html")

    except Exception as e:
        print(f"Ops, something gone wrong: {e}")
        return render(request, "error.html")


def authenticaiton(request):
    try:
        redirect_url = f'{os.environ.get("DOMAIN_OR_IP")}/converter/converter'
        print("FOR DEBUG: ", redirect_url)
        auth_url = f'https://accounts.spotify.com/authorize?client_id={os.environ.get("SPOTI_CLIENT_ID")}&response_type=code&redirect_uri={redirect_url}&scope=playlist-modify-public user-read-private user-library-read'
        return redirect(auth_url)

    except Exception as e:
        print(f"Ops, something gone wrong: {e}")
        return render(request, "error.html")


def converter(request):
    return render(request, "converter.html")


def end(request):
    return render(request, "end.html")
