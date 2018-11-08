from flask import Blueprint
from flask_restful import Api
from .views import Registration, SignIn

auth = Blueprint('auth', __name__, url_prefix="/auth/v1")

api = Api(auth)

api.add_resource(Registration, '/register')
api.add_resource(SignIn, '/login')
