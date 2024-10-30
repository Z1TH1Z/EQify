import time
from Artistid import get_current_track
from Artistid import get_genre_artist
from Refresh_token import refresh_access_token

CLIENT_ID = '326637050557468ebdf9967fb97562a2'
CLIENT_SECRET = '306a96444b384daea5ebac33ec7c141f'
REFRESH_TOKEN = "AQCtGs9fyHNGF3xlgqrz1BGb5D7oV8fb6p1l2nVRL_9xem71i3IQlkxmdTzHreZ07TGpu0-b111wOSR_3bYYd4Yut8aESOoxpW3SRk2h0HxeyDMrhHA2-yEs1oqw5LDj8hk"

# Set the refresh interval (60 minutes)
REFRESH_INTERVAL = 60 * 60  # in seconds


def main():
    # Initial token refresh
    SPOTIFY_ACCESS_TOKEN = refresh_access_token(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
    last_refresh_time = time.time()

    while True:
        current_time = time.time()

        # Check if 60 minutes have passed
        if current_time - last_refresh_time >= REFRESH_INTERVAL:
            SPOTIFY_ACCESS_TOKEN, _ = refresh_access_token(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
            last_refresh_time = current_time  # Update the last refresh time

        # Fetch current track info and genre
        current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
        get_genre = get_genre_artist(SPOTIFY_ACCESS_TOKEN)

        print(get_genre)

        # Sleep for a short duration before the next iteration
        time.sleep(0.1)


if __name__ == '__main__':
    main()