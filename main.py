import time
from Artistid import get_current_track
from Artistid import get_genre_artist


def main():
    # Read access token from file
    with open("access_token.txt", "r") as act:
        SPOTIFY_ACCESS_TOKEN = act.readline().strip()

    while True:
        # Get current track information
        current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)

        # Print the current track information
        #print(current_track_info)

        get_genre = get_genre_artist(SPOTIFY_ACCESS_TOKEN)
        print(get_genre)

        time.sleep(0.1)


if __name__ == '__main__':
    main()