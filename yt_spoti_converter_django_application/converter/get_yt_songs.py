import requests
import json

def get_yt_songs(yt_api_key, yt_playlist_id):
    try:
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={yt_playlist_id}&key={yt_api_key}"

        yt_song_list = []
        # saves all YT video names into a list
        while True:
            response = requests.get(url)
            data = json.loads(response.text)

            for item in data["items"]:
                yt_song_list.append(item["snippet"]["title"])

            # data is paginated, this is required
            if "nextPageToken" in data:
                url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={yt_playlist_id}&key={yt_api_key}&maxResults=50&pageToken={data['nextPageToken']}"
            else:
                break    

        return yt_song_list 
           
    except Exception as e:
        print(f"Ops, something gone wrong in get_yt_songs: {e}")