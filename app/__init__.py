from flask import Flask, Blueprint
from app import config
from app.api.v1 import version1
from app.api.v2 import version2
from app.api.v2.dbmodel import SenditDb
from app.auth.v1 import auth
from app.auth.v2 import auth2

#from . import config
#from .api.v1 import version1
#from .api.v2 import version2
#from .api.v2.dbmodel import SenditDb
#from .auth.v1 import auth
#from .auth.v2 import auth2

def create_app(config_option="DevConfig"):
    """
    Initialize the app for a development environment
    """
    app = Flask(__name__)
    app.config.from_object(config.config[config_option])
    SenditDb.start_db('postgres://vhgobajxbehppp:b05d8b59b7552e74c763d86945c5b29c2fd11c5e000cfc417190eca27f8eb3d5@ec2-54-204-40-248.compute-1.amazonaws.com:5432/d4v7duckviarp9')
    SenditDb.build_all()
    app.register_blueprint(version1)
    app.register_blueprint(version2)
    app.register_blueprint(auth)
    app.register_blueprint(auth2)
    return app


