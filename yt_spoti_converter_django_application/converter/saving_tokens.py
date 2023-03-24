import os
import requests
import json

def saving_tokens(request):
    print("STEP ONE")
    # POST method - Getting YT playlist ID
    if request.method == "POST":
        print("STEP TREE")
        yt_playlist_id = request.GET.get("list", "")
        request.session["yt_playlist_id"] = yt_playlist_id

    # GET method - Getting Spotify tokens
    elif request.method == "GET":
        print("STEP TWO")
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

        headers = {
            "Authorization": "Bearer " + request.session['spoti_access_token']
        }
        response = requests.get("https://api.spotify.com/v1/me", headers=headers)
        spoti_user_id = json.loads(response.text)["id"]

        request.session["spoti_user_id"] = spoti_user_id
