from flask import Blueprint
from flask_restful import Api
from .views import ParcelList

version1 = Blueprint('v1', __name__, url_prefix="/api/v1")

api = Api(version1)

api.add_resource(ParcelList, '/parcels')