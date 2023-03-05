from flask import (Blueprint, request)

from . import mongo

bp = Blueprint('adduser', __name__, url_prefix='/db')

@bp.route('/adduser', methods=['POST'])
def addUser():
    data = request.json
    print (data)

    try:
        x = mongo.addUser(data['email'], data['access_token'], data['refresh_token'])
        print(x)
        return {"id": x}
    except:
        return {"id":400}