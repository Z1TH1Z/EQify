import requests


def refresh_access_token(client_id, client_secret, refresh_token):
    url = "https://accounts.spotify.com/api/token"

    # Prepare the data for the POST request
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret
    }

    # Make the POST request to refresh the access token
    response = requests.post(url, data=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        token_info = response.json()
        access_token = token_info['access_token']
        expires_in = token_info['expires_in']


        return access_token
    else:
        print("Failed to refresh access token:", response.status_code, response.text)
        return None, None


if __name__ == "__main__":
    CLIENT_ID = '326637050557468ebdf9967fb97562a2'
    CLIENT_SECRET = '306a96444b384daea5ebac33ec7c141f'
    REFRESH_TOKEN = "AQCtGs9fyHNGF3xlgqrz1BGb5D7oV8fb6p1l2nVRL_9xem71i3IQlkxmdTzHreZ07TGpu0-b111wOSR_3bYYd4Yut8aESOoxpW3SRk2h0HxeyDMrhHA2-yEs1oqw5LDj8hk"

    new_access_token = refresh_access_token(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)