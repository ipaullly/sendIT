from flask import Blueprint
from flask_restful import Api
#from .views import Registration
auth_version1 = Blueprint('v1', __name__, url_prefix="/auth/v1")

api = Api(auth_version1)

#api.add_resource(Registration, '/register')
