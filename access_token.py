import requests
import base64
import json
from flask import Flask, request, redirect

# Replace these with your Spotify app credentials
CLIENT_ID = '326637050557468ebdf9967fb97562a2'
CLIENT_SECRET = '306a96444b384daea5ebac33ec7c141f'
REDIRECT_URI = 'http://localhost:8888/callback'
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
SCOPES = 'user-read-currently-playing user-read-playback-state'

app = Flask(__name__)

# Step 1: Redirect the user to Spotify's authorization page
@app.route('/')
def login():
    auth_query_parameters = {
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "scope": SCOPES,
    }
    url_args = "&".join([f"{key}={val}" for key, val in auth_query_parameters.items()])
    auth_url = f"{AUTH_URL}/?{url_args}"
    return redirect(auth_url)

# Step 2: Handle Spotify's callback and exchange the authorization code for an access token
@app.route('/callback')
def callback():
    auth_code = request.args['code']
    auth_header = base64.urlsafe_b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

    token_data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": REDIRECT_URI
    }

    token_headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(TOKEN_URL, data=token_data, headers=token_headers)

    if response.status_code == 200:
        token_info = response.json()
        access_token = token_info['access_token']

        # Write token info to a text file
        with open('access_token.txt', 'w') as token_file:
            token_file.write(f"{access_token}")

        return "Access tokens have been written to access_token.txt."

    return f"Failed to get token: {response.status_code}, {response.text}"

if __name__ == '__main__':
    app.run(debug=True, port=8888)