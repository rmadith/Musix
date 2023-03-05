import json
import sys
import time

sys.path.append("/home/muthu/Musix/Algorithm")
sys.path.append("/home/muthu/Musix/Backend/authorization")
import HashedQueue
import Song

import Spotify
import threading
from flask import (Blueprint, request)

from . import mongo

bp = Blueprint('adduser', __name__, url_prefix='/db')

supremeHash = {}

@bp.route('/adduser', methods=['POST'])
def addUsermethod():
    data = request.json
    try:
        x = mongo.addUser(data["email"], data["access_token"], data["refresh_token"])
        return {"id": str(x)}
    except:
        return {"id":400}
    

@bp.route('/getUserSession', methods=['POST'])
def getUserSession():
    data = request.json
    try:
        x = mongo.getUserSession(data["id"])
        return x
    except:
        return {"id":400}
    
@bp.route('/createsession', methods=['POST'])
def createsession():
    data = request.json
    try:
        x = mongo.createsession(data["host_id"], data["type_id"])
        y = mongo.addUserToSession(x, data["host_id"])
        supremeHash[str(x)] = HashedQueue.HashedQueue()
        try:
            playlist = Spotify.getplaylist( str(y["access_token"]), str(data["type_id"]))
        except Exception as e:
            print(e)
        print(playlist)
        for song in playlist["tracks"]["items"]:
            supremeHash[str(x)].add(Song.Song(song["track"]["album"]["name"], song["track"]["album"]["uri"], song["track"]["album"]["images"][0]["url"]))
        t1 = threading.Thread(target=enqueue(), args=(str(x), y["access_token"],))
        t1.start()
        return {"id": str(x)}
    except:
        return {"id":400}
    
    
@bp.route('/addUserToSession', methods=['PUT'])
def addUserToSession():
    data = request.json
    try:
        x = mongo.addUserToSession(data["session_id"], data["user_id"])
        y = mongo.addUserToSession(x, data["user_id"])
        playlist = Spotify.getplaylist( y["access_token"], data["type_id"])
        for i in playlist["tracks"]["items"]:
            supremeHash[str(data["session_id"])].add(Song.Song(i["track"]["album"]["name"], i["track"]["album"]["uri"], i["track"]["album"]["images"][0]["url"]))
        return {"id": str(x)}
    except:
        return {"id":400}
    

@bp.route('/deleteSession', methods=['DELETE'])
def deleteSession():
    data = request.json
    try:
        x = mongo.deleteSession(data["session_id"])
        return {"id": str(x)}
    except:
        return {"id":400}

@bp.route('/deleteUserFromSession', methods=['DELETE'])
def deleteUserFromSession():
    data = request.json
    try:
        x = mongo.deleteUserFromSession(data["session_id"], data["user_id"])
        return {"id": str(x)}
    except:
        return {"id":400}
    
@bp.route('/get-participants', methods=['POST'])
def getParticipants():
    data = request.json
    try:
        x = mongo.getUsersinSession(data["session_id"])
        print(x)
        return x
    except:
        return {"id":400}
    
@bp.route('/get-auth', methods=['POST'])
def getAuth():
    data = request.json
    try:
        x = mongo.getAuth(data["user_id"])
        return {"access_token": x}
    except:
        return {"id":400}
    


def enqueue(args, auth):
    while(1):
        for i in range(1,5):
            Song = supremeHash[str(args)].pop()
            Spotify.addtoQueue(auth, Song.trackId)
        time.sleep(60)