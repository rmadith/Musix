from flask import (Blueprint, request, json, session)

import os
import requests
import base64
import json
from secrets import *

from . import Spotify


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

    headers['Authorization'] = f"Basic {base64_message}"
    data['grant_type'] = 'authorization_code'
    data['code'] = code
    data['redirect_uri'] = 'http://64.33.187.77:8000'

    r = requests.post(url, headers=headers, data=data)

    tokens = r.json()

    print(tokens)

    res = Spotify.getme(tokens['access_token'])

    print(res)
    session.clear()


    return {"hello":"world"}