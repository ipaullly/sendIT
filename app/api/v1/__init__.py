from flask import Blueprint
from flask_restful import Api


version1 = Blueprint('v1', __name__, url_prefix="/api/v1")

api = Api(version1)