from flask import Blueprint
from flask_restful import Api
from app.auth.v2.views import SignUp, SignIn

auth2 = Blueprint('authV2', __name__, url_prefix="/auth/v2")

api = Api(auth2)

api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/login')