from flask import (Blueprint, request)

from . import mongo

bp = Blueprint('adduser', __name__, url_prefix='/db')

@bp.route('/adduser', methods=['POST'])
def addUser():
    data = request.json
    print (data)

    try:
        x = mongo.addUser("hello", "Hi","howreyou")
        print(x)
        return {"id": x}
    except:
        return {"id":400}
    
    return {"id":401}