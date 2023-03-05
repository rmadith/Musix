from flask import (Blueprint, request, json, session, make_response, render_template, redirect)

import os
import requests
import base64
import json
from secrets import *
import datetime

from flask_cors import CORS,cross_origin
from . import Spotify

import uuid

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
    data['redirect_uri'] = 'https://musix-two.vercel.app/login'

    r = requests.post(url, headers=headers, data=data)

    tokens = r.json()

    print(tokens)

    access_token = tokens['access_token']

    res = Spotify.getme(access_token)

    print(res)

    user = res

    user_object = {
        'id': uuid.uuid1(),
        'name': user['display_name'],
        'email': user['email'],
        'activeSession': [],
        'topArtists': [],
        'topTracks': [],
        'streaming': False
    }

    return user_object
