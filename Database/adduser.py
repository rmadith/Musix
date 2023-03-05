from flask import (Blueprint, request)

from . import mongo

bp = Blueprint('login', __name__, url_prefix='/')

@bp.route('/adduser', methods=['POST'])
def addUser():
    data = request.json
    try:
        x = mongo.addUser(data['email'], data['access_token'], data['refresh_token'])
        return {"id": x}
    except:
        return 400
    return 