import os
import requests
import json


def saving_tokens(request):
    # Getting YT playlist ID
    if request.method == "POST":
        yt_link = request.POST.get("yt_link")
        playlist_id = yt_link.split("?list=")[1]
        request.session["yt_playlist_id"] = playlist_id

    # Getting Spotify tokens
    elif request.method == "GET":
        # access_token setup
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

        # access_token request
        while True:
            try:
                access_token_response = requests.post(token_url, data=data, auth=auth)
                break
            except requests.exceptions.RequestException as e:
                print(e)

        # validating access_token
        if access_token_response.status_code != 200:
            raise Exception("Token API response ERROR!")

        if access_token_response == None:
            raise Exception("Token API response is empty!")

        # user_id setup
        headers = {
            "Authorization": "Bearer " + access_token_response.json()["access_token"]
        }

        # user_id request
        while True:
            try:
                user_id_response = requests.get(
                    "https://api.spotify.com/v1/me", headers=headers
                )
                break
            except requests.exceptions.RequestException as e:
                print(e)

        # valdiating user_id
        if user_id_response.status_code != 200:
            raise Exception("Token API response ERROR!")

        if user_id_response == None:
            raise Exception("Token API response is empty!")

        # sessions setup
        access_token = access_token_response.json()["access_token"]
        request.session["spoti_access_token"] = access_token

        spoti_user_id = json.loads(user_id_response.text)["id"]
        request.session["spoti_user_id"] = spoti_user_id
