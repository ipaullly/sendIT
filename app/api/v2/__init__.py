from flask import Blueprint
from flask_restful import Api
from .views import ParcelList, SingleParcel, ParcelStatus, ParcelLocation, CancelParcel, UserOrders

version2 = Blueprint('v2', __name__, url_prefix="/api/v2")

api = Api(version2)

api.add_resource(ParcelList, '/parcels')
api.add_resource(SingleParcel, '/parcels/<int:id>/destination')
api.add_resource(ParcelStatus, '/parcels/<int:id>/status')
api.add_resource(ParcelLocation, '/parcels/<int:id>/presentLocation')
api.add_resource(CancelParcel, '/parcels/<int:id>/cancel')
api.add_resource(UserOrders, '/users/<int:id>/parcels')