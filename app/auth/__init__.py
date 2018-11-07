from flask import Blueprint
from flask_restful import Api
from .views import Registration

auth = Blueprint('auth', __name__, url_prefix="/auth")

api = Api(auth)

api.add_resource(Registration, '/register')
