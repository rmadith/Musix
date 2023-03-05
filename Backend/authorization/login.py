from flask import (Blueprint, request, json)

import os
import requests
import base64
import json
from secrets import *
import sys


sys.path.insert(0, "/home/muthu/Musix/Backend/authorization")
import Spotify

bp = Blueprint('login', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():

    data = request.json

    # make sure we have code before hand

    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')

    code = data['code']

    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}   


    # Encode as Base64
    message = f"{client_id}:{client_secret}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    headers['Authorization'] = f"Basic {str(base64_message)}"
    headers['Content-Type'] = 'application/x-www-form-urlencoded'

    data['grant_type'] = 'authorization_code'
    data['code'] = code
    data['redirect_uri'] = 'http://localhost:3000/login'

    r = requests.post(url, headers=headers, data=data)

    tokens = r.json()

    print(tokens)

    access_token = tokens['access_token']
    top_artists = Spotify.gettop(access_token, 'artists')
    if top_artists == False:
        return {"error": "Unauthorized"}
    
    top_artists = top_artists['items']
    top_artists_response = [
            {
                'name': top_artists[0]['name'],
                'image': top_artists[0]["images"][0]["url"],
            },
            {
                'name': top_artists[1]['name'],
                'image': top_artists[1]["images"][0]["url"],
            },
            {
                'name': top_artists[2]['name'],
                'image': top_artists[2]["images"][0]["url"],
            }
        ]
    

    top_tracks = Spotify.gettop(access_token, 'tracks')
    if top_tracks == False:
        return {"error": "Unauthorized"}
    
    top_tracks = top_tracks['items']
    top_tracks_response = [
            {
                'name': top_tracks[0]['name'],
                'image': top_tracks[0]['album']['images'][0]['url'],
                'artist': top_tracks[0]['artists'][0]['name']
            },
            {
                'name': top_tracks[1]['name'],
                'image': top_tracks[1]['album']['images'][0]['url'],
                'artist': top_tracks[1]['artists'][0]['name']
            },
            {
                'name': top_tracks[2]['name'],
                'image': top_tracks[2]['album']['images'][0]['url'],
                'artist': top_tracks[2]['artists'][0]['name']
            }
        ]

    res = Spotify.getme(access_token)

    user = res
    url = "http://64.33.187.77:8000/db/adduser"

    payload = json.dumps({
        'email': user['email'],
        'access_token': access_token,
        'refresh_token': tokens['refresh_token']
    })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    url = "http://64.33.187.77:8000/db/getUserSession"

    data = json.dumps({
        'id': response.json()['id']
    })

    response_3 = requests.request("POST", url, headers=headers, data=data)

    url = "http://64.33.187.77:8000/db/getStreaming"

    response_4 = requests.request("POST", url, headers=headers, data=data)

    user_object = {
        'id': response.json()['id'],
        'name': user['display_name'],
        'email': user['email'],
        'activeSessions': list(response_3.json().keys()),
        'topArtists': top_artists_response,
        'topTracks': top_tracks_response,
        'streaming': response_4.json()["streaming"],
        'access_token': access_token
    }

    return user_object
