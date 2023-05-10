import requests
import json


def add_spoti_songs(spoti_token, spoti_playlist_id, yt_song_list):
    for song in yt_song_list:
        headers = {"Authorization": "Bearer " + spoti_token}
        search_url = f"https://api.spotify.com/v1/search?q={song}&type=track&limit=1"
        # request exceptions
        while True:
            try:
                response = requests.get(search_url, headers=headers)
                break
            except requests.exceptions.RequestException as e:
                print(e)

        # validating response
        if response.status_code != 200:
            raise Exception("Spoti API response ERROR!")

        if response == None:
            raise Exception("Spoti API response is empty!")

        song_id = response.json()["tracks"]["items"][0]["id"]
        headers = {
            "Authorization": "Bearer " + spoti_token,
            "Content-Type": "application/json",
        }
        add_url = f"https://api.spotify.com/v1/playlists/{spoti_playlist_id}/tracks?uris=spotify:track:{song_id}"
        # for request exceptions
        while True:
            try:
                response = requests.post(add_url, headers=headers)
                break
            except requests.exceptions.RequestException as e:
                print(e)

        # validating response
        if response.status_code != 201:
            raise Exception("Spoti API response ERROR!")
