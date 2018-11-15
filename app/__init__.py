from flask import Flask, Blueprint
from .api.v1 import version1
from .auth.v1 import auth
#from db_config import create_tables, destroy_tables

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    #create_tables()
    app.config.from_pyfile('config.py')
    app.register_blueprint(version1)
    app.register_blueprint(auth)

    return app