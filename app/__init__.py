from flask import Flask, Blueprint
from .api.v1 import version1
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.register_blueprint(version1)
    app.register_blueprint(auth)

    return app