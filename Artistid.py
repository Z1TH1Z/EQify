import requests
from pprint import pprint

with open("access_token.txt", "r+") as act:
    SPOTIFY_ACCESS_TOKEN = act.readline()
SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player'


def get_current_track(access_token):
    response = requests.get(SPOTIFY_GET_CURRENT_TRACK_URL,
                            headers={
                                "Authorization": f"Bearer {access_token}"  # Added space after 'Bearer'
                            }
                            )

    # Check if the request was successful
    if response.status_code != 200:
        return {"error": f"Failed to fetch track: {response.status_code} {response.text}"}

    resp_json = response.json()

    # Check if there is currently playing track
    if 'item' not in resp_json:
        return {"error": "No track is currently playing."}

    track_id = resp_json['item']['id']
    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists']
    artists_names = ', '.join([artist['name'] for artist in artists])
    link = resp_json['item']['external_urls']['spotify']
    ##artist_id = resp_json['item']['artist']['id']
    artist_ids = ', '.join([artist['id'] for artist in resp_json['item']['artists']])
    duration = int(resp_json['item']['duration_ms'])
    duration = round(duration / 60000 , 2)
    current_track_info = {
        "id": track_id,
        "name": track_name,
        "artists": artists_names,
        "link": link,
        "artist_id": artist_ids,
        "Length of the song" : duration
    }

    return current_track_info
#artist_id = get_current_track(SPOTIFY_ACCESS_TOKEN)["artist_id"]
#s_g_gen_url = f"https://api.spotify.com/v1/artists/{artist_id.split(", ")[0]}"
def get_genre_artist(S_A_C):
    artist_id = get_current_track(SPOTIFY_ACCESS_TOKEN)["artist_id"]
    s_g_gen_url = f"https://api.spotify.com/v1/artists/{artist_id.split(", ")[0]}"
    response = requests.get(s_g_gen_url,
                            headers={
                                "Authorization": f"Bearer {S_A_C}"  # Added space after 'Bearer'
                            }
                            )

    # Check if the request was successful
    if response.status_code != 200:
        return {"error": f"Failed to fetch track: {response.status_code} {response.text}"}

    resp_json = response.json()
    genres = resp_json.get('genres', [])  # Safely get genres, default to empty list
    genre_list = ', '.join(genres)  # Join genres into a string

    return genre_list
def main():
    #current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
    #pprint(current_track_info, indent=4)
    get_genre = get_genre_artist(SPOTIFY_ACCESS_TOKEN)
    print(get_genre)
#spotify_artist_id = get_current_track(SPOTIFY_ACCESS_TOKEN)['artist_id']
#print(spotify_artist_id)

if __name__ == '__main__':
    main()

