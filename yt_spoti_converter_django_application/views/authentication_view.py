from django.shortcuts import render
import os
from django.shortcuts import redirect


def authenticaiton(request):
    redirect_url = f'{os.environ.get("DOMAIN_OR_IP")}/converter/converter'
    auth_url = f'https://accounts.spotify.com/authorize?client_id={os.environ.get("SPOTI_CLIENT_ID")}&response_type=code&redirect_uri={redirect_url}&scope=playlist-modify-public user-read-private user-library-read'
    return redirect(auth_url)

