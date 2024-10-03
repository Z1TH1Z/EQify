from Artistid import spotify_artist_id
import requests
with open("access_token.txt", "r+") as act:
    s_a_c = act.readline()
s_g_gen_url = f"https://api.spotify.com/v1/artists/{spotify_artist_id.split(", ")[0]}"

def get_genre_artist(s_a_c):
    response = requests.get(s_g_gen_url,
                            headers={
                                "Authorization": f"Bearer {s_a_c}"  # Added space after 'Bearer'
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
    get_genre = get_genre_artist(s_a_c)
    print(get_genre)

if __name__ == '__main__':
    main()