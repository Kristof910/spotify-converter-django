from .create_spoti_playlist import create_spoti_playlist
from .add_spoti_songs import add_spoti_songs
from .get_yt_songs import get_yt_songs
from celery import Celery

app = Celery("converting_manager", broker="pyamqp://guest@localhost//")


@app.task
def converting_manager(request):
    yt_playlist_id = request["yt_playlist_id"]
    spoti_token = request["spoti_access_token"]
    spoti_user_id = request["spoti_user_id"]
    yt_api_key = request["YT_API_KEY"]
    spoti_playlist_name = request["spoti_playlist_name"]

    yt_song_list = get_yt_songs(yt_api_key, yt_playlist_id)
    spoti_playlist_id = create_spoti_playlist(
        spoti_token, spoti_user_id, spoti_playlist_name
    )
    add_spoti_songs(spoti_token, spoti_playlist_id, yt_song_list)
