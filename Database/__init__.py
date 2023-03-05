from flask import Flask
from flask_cors import CORS




def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from . import adduser
    app.register_blueprint(adduser.bp)

    CORS(app)
    return app
