import requests
from pprint import pprint
from Refresh_token import refresh_access_token
CLIENT_ID = '326637050557468ebdf9967fb97562a2'
CLIENT_SECRET = '306a96444b384daea5ebac33ec7c141f'
REFRESH_TOKEN = "AQCtGs9fyHNGF3xlgqrz1BGb5D7oV8fb6p1l2nVRL_9xem71i3IQlkxmdTzHreZ07TGpu0-b111wOSR_3bYYd4Yut8aESOoxpW3SRk2h0HxeyDMrhHA2-yEs1oqw5LDj8hk"


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player'
SPOTIFY_ACCESS_TOKEN = refresh_access_token(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
def get_current_track(access_token):
    response = requests.get(SPOTIFY_GET_CURRENT_TRACK_URL,
                            headers={
                                "Authorization": f"Bearer {access_token}"
                            }
                            )


    if response.status_code != 200:
        return {"error": f"Failed to fetch track: {response.status_code} {response.text}"}

    resp_json = response.json()

    if 'item' not in resp_json:
        return {"error": "No track is currently playing."}

    track_id = resp_json['item']['id']
    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists']
    artists_names = ', '.join([artist['name'] for artist in artists])
    link = resp_json['item']['external_urls']['spotify']
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
    genres = resp_json.get('genres', [])
    genre_list = ', '.join(genres)

    return genre_list
def main():
    get_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
    track_name = get_track_info['name']
    get_genre = get_genre_artist(SPOTIFY_ACCESS_TOKEN)
    print(get_genre)


if __name__ == '__main__':
    main()

