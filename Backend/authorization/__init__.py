from flask import Flask
from flask_cors import CORS

from dotenv import load_dotenv


def create_app():
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev"
    )

    from . import login
    from . import session

    app.register_blueprint(login.bp)
    app.register_blueprint(session.bp)

    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    return app
