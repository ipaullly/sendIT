from flask import Blueprint
from flask_restful import Api
from .views import ParcelList #, IndividualParcel, CancelParcel, UserOrders

vern2 = Blueprint('v2', __name__, url_prefix="/api/v2")

api = Api(vern2)

api.add_resource(ParcelList, '/parcels')
#api.add_resource(IndividualParcel, '/parcels/<int:id>')
#api.add_resource(UserOrders, '/user/<string:id>/parcels')
#api.add_resource(CancelParcel, '/parcels/<int:id>/cancel')