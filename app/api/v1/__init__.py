from flask import Blueprint
from flask_restful import Api
from .views import ParcelList, IndividualParcel, CancelParcel

version1 = Blueprint('v1', __name__, url_prefix="/api/v1")

api = Api(version1)

api.add_resource(ParcelList, '/parcels')
api.add_resource(IndividualParcel, '/parcels/<int:id>')
api.add_resource(CancelParcel, '/parcels/<int:id>/cancel')