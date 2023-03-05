from flask import (Blueprint, request, json)
import sys

sys.path.insert(0, "/home/muthu/Musix/Backend/authorization")
import requests

bp = Blueprint('session', __name__, url_prefix='/sessions')


@bp.route('/create-session', methods=['POST'])
def createsession():
    data = request.json
    url = "http://64.33.187.77:8000/db/createsession"

    payload = json.dumps({
        'host_id': data['creatorId'],
        "type_id": data['themeId']
    })

    headers = {
    'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
    except:
        return "Error", 400

    return response.json(), 200

@bp.route('/join-session', methods=['PUT'])
def joinSession():
    data = request.json
    url = "http://64.33.187.77:8000/db/addUserToSession"

    payload = json.dumps({
        'session_id': data['sessionId'],
        'user_id': data['userId'],
    })

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("PUT", url, headers=headers, data=payload)
    except:
        return "Error", 400
    
    return "Success", 200

@bp.route('/delete-session', methods=['DELETE'])
def deleteSession():
    data = request.json
    url = "http://64.33.187.77:8000/db/deleteSession"
    payload = json.dumps({
        'session_id': data['sessionId']
    })
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("DELETE", url, headers=headers, data=payload)
    except:
        return "Error", 400
    return "Success", 200

@bp.route('/leave-session', methods=['DELETE'])
def leaveSession():
    data = request.json
    url = "http://64.33.187.77:8000/db/deleteUserFromSession"
    payload = json.dumps({
        'session_id': data['sessionId'],
        'user_id': data['userId']
    })
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("DELETE", url, headers=headers, data=payload)
    except:
        return "Error", 400
    return "Success", 200

@bp.route('/get-particpants', methods=['GET'])
def getParticipants():
    data = request.args.get('sessionId')
    url = "http://64.33.187.77:8000/db/get-participants"
    payload = json.dumps({
        'session_id': data['sessionId']
    })
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except:
        return "Error", 400
    
    return response.json(), 200

@bp.route('/add-song', methods=['POST'])
def addSong():
    data = request.json
    trackId = data['trackId']
    sessionId = data['sessionId']

