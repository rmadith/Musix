from flask import Flask
from flask_cors import CORS

from dotenv import load_dotenv


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from . import login

    app.register_blueprint(login.bp)

    CORS(app)
    return app
