import requests
import json

def add_spoti_songs(spoti_token, spoti_playlist_id, yt_song_list):
    try:
        for song in yt_song_list:
            headers = {'Authorization': 'Bearer ' + spoti_token}
            search_url = f'https://api.spotify.com/v1/search?q={song}&type=track&limit=1'
            response = requests.get(search_url, headers=headers)
            song_id = response.json()['tracks']['items'][0]['id']

            headers = {'Authorization': 'Bearer ' + spoti_token, 'Content-Type': 'application/json'}
            add_url = f'https://api.spotify.com/v1/playlists/{spoti_playlist_id}/tracks?uris=spotify:track:{song_id}'
            response = requests.post(add_url, headers=headers)

    except Exception as e:
        print(f"Ops, something gone wrong in add_spoti_songs: {e}")