from flask import (Blueprint, request, json, session, make_response, render_template)

import os
import requests
import base64
import json
from secrets import *
import datetime


from . import Spotify


bp = Blueprint('login', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'], supports_credentials=True, headers=['Content-Type', 'Authorization'], origin='javin.jmsgvn.com')
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

    # session.clear()
    # session['domain'] = "localhost:3000"
    # session["user_email"] = user["email"]

    expire_date = datetime.datetime.now()
    expire_date = expire_date + datetime.timedelta(days=90)

    resp = make_response()
    resp.set_cookie('somecookiename', 'I am cookie', expires=expire_date, secure=True, httponly=True, samesite='None')

    return resp