from flask import Flask, Blueprint
from . import config
from .api.v1 import version1
from .api.v2 import vern2
from .api.v2.dbmodel import SenditDb
from .auth.v1 import auth
#from db_config import create_tables, destroy_tables

def create_app(config_option="DevConfig"):
    """
    Initialize the app for a development environment
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config.config[config_option])
    SenditDb.start_db(app.config['DATABASE_URI'])
    SenditDb.build_all()
    app.register_blueprint(version1)
    app.register_blueprint(vern2)
    app.register_blueprint(auth)
    return app


