from django.shortcuts import render
from ..converter.converting_manager import converting_manager
from ..tasks import tasks
import os


def end(request):
    request_dict = {
        "yt_playlist_id": request.session["yt_playlist_id"],
        "spoti_access_token": request.session["spoti_access_token"],
        "spoti_user_id": request.session["spoti_user_id"],
        "YT_API_KEY": os.environ.get("YT_API_KEY"),
        "spoti_playlist_name": "YT Converted",
    }

    tasks.delay(request_dict)

    return render(request, "end.html")
