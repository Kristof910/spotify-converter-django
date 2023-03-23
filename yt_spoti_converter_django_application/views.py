from django.shortcuts import render
import os
from django.shortcuts import redirect
import json
import requests


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
        print(f"Ops, something gone wrong in index: {e}")
        return render(request, "error.html")


def authenticaiton(request):
    try:
        redirect_url = f'{os.environ.get("DOMAIN_OR_IP")}/converter/converter'
        print("FOR DEBUG: ", redirect_url)
        auth_url = f'https://accounts.spotify.com/authorize?client_id={os.environ.get("SPOTI_CLIENT_ID")}&response_type=code&redirect_uri={redirect_url}&scope=playlist-modify-public user-read-private user-library-read'
        return redirect(auth_url)

    except Exception as e:
        print(f"Ops, something gone wrong in authentication: {e}")
        return render(request, "error.html")


def converter(request):
    try:
        # POST method
        if request.method == "POST":
            yt_playlist_id = request.GET.get("list", "")

            request.session["yt_playlist_id"] = yt_playlist_id
            return redirect("end")

        # GET method
        code = request.GET.get("code", "")
        token_url = "https://accounts.spotify.com/api/token"
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": f'{os.environ.get("DOMAIN_OR_IP")}/converter/converter',
        }
        auth = (
            os.environ.get("SPOTI_CLIENT_ID"),
            os.environ.get("SPOTI_CLIENT_SECRET"),
        )
        response = requests.post(token_url, data=data, auth=auth)
        access_token = response.json()["access_token"]

        request.session["spoti_access_token"] = access_token
        return render(request, "converter.html")

    except Exception as e:
        print(f"Ops, something gone wrong in converter: {e}")
        return render(request, "error.html")


def end(request):
    return render(request, "end.html")
