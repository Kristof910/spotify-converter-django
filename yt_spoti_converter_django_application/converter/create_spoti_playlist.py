import requests
import json


def create_spoti_playlist(spoti_token, spoti_user_id, spoti_playlist_name):
    headers = {
        "Authorization": "Bearer " + spoti_token,
        "Content-Type": "application/json",
    }

    playlist_data = {
        "name": spoti_playlist_name,
        "description": "This playlist has been converted from YouTube",
    }
    # for request exceptions
    while True:
        try:
            response = requests.post(
                f"https://api.spotify.com/v1/users/{spoti_user_id}/playlists",
                headers=headers,
                data=json.dumps(playlist_data),
            )
            break
        except requests.exceptions.RequestException as e:
            print(e)
    return response.json()["id"]
