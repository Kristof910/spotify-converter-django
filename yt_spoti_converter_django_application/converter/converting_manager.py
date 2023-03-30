from .create_spoti_playlist import create_spoti_playlist
from .add_spoti_songs import add_spoti_songs
from .get_yt_songs import get_yt_songs
import os
import pdb


def converting_manager(request):
    yt_playlist_id = request.session["yt_playlist_id"]
    spoti_token = request.session["spoti_access_token"]
    spoti_user_id = request.session["spoti_user_id"]
    yt_api_key = os.environ.get("YT_API_KEY")
    spoti_playlist_name = "YT Converted"

    yt_song_list = get_yt_songs(yt_api_key, yt_playlist_id)
    spoti_playlist_id = create_spoti_playlist(
        spoti_token, spoti_user_id, spoti_playlist_name
    )
    add_spoti_songs(spoti_token, spoti_playlist_id, yt_song_list)
