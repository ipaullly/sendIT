from flask import Blueprint
from flask_restful import Api
from .views import ParcelList, SingleParcel #, IndividualParcel, CancelParcel, UserOrders

version2 = Blueprint('v2', __name__, url_prefix="/api/v2")

api = Api(version2)

api.add_resource(ParcelList, '/parcels')
api.add_resource(SingleParcel, '/parcels/<int:id>')
#api.add_resource(UserOrders, '/user/<string:id>/parcels')
#api.add_resource(CancelParcel, '/parcels/<int:id>/cancel')