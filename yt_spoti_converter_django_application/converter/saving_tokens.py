import os
import requests

def saving_tokens(request):

    # POST method
    if request.method == "POST":
        yt_playlist_id = request.GET.get("list", "")

        request.session["yt_playlist_id"] = yt_playlist_id

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