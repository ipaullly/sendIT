from flask import Flask, Blueprint
from instance.config import DevConfig
from .api.v1 import version1
from .auth.v1 import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    app.register_blueprint(version1)
    app.register_blueprint(auth)

    return app