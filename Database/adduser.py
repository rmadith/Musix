from flask import (Blueprint, request)

from . import mongo

bp = Blueprint('adduser', __name__, url_prefix='/db')

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
        testid = mongo.getUser(data["host_id"])
        print(testid)
        y = mongo.addUserToSession(x, data["host_id"])
        return {"id": str(x)}
    except:
        return {"id":400}
    
    
@bp.route('/addUserToSession', methods=['PUT'])
def addUserToSession():
    data = request.json
    try:
        x = mongo.addUserToSession(data["session_id"], data["user_id"])
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
        y = []
        for i in x:
            x[i] = mongo.getUser(i)
            y.append(x[i]["email"])
        return {"participants": y}
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
    

    