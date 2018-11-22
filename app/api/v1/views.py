from flask_restful import Resource
from flask import make_response, jsonify, request
from app.api.v1.models import Parcels
from app.utilities.validation_functions import check_for_space

order = Parcels()

class ParcelList(Resource):
    """
    class for Create order and retrieve list of orders API endpoints
    """
    def post(self):
        """
        post method to add new order to list of orders
        """
        data = request.get_json()
        item = data['item']
        pickup = data['pickup']
        dest = data['dest']
        pricing = data['pricing']
        author = data['user_id']

        if check_for_space(item):
            if check_for_space(pickup):
                if check_for_space(dest):
                    if check_for_space(pricing):
                        if check_for_space(author):
                            res = order.create_order(item, pickup, dest, pricing, author)
                            return make_response(jsonify({
                                "message" : "delivery order created successfully",
                                "new delivery order" : res
                            }), 201)
                        else:
                            return make_response(jsonify({
                                "message" : "Invalid user id"
                            }), 400) 
                    else:
                        return make_response(jsonify({
                            "message" : "Invalid price value"
                        }), 400) 
                else:
                    return make_response(jsonify({
                        "message" : "Invalid destination name"
                    }), 400) 
            else:
                return make_response(jsonify({
                    "message" : "Invalid pickup location name"
                }), 400) 
        else:
           return make_response(jsonify({
                "message" : "Invalid item name format"
            }), 400) 

    def get(self):
        """
        get method to retrieve list of all orders
        """
        resp = order.order_list()
        return make_response(jsonify({
            "message" : "ok",
            "Delivery Orders" : resp
        }), 200)

class IndividualParcel(Resource):
    """
    class for API endpoints for retrieving single order and cancelling particular order
    """
    def get(self, id):
        """
        get method to retrieve order by id
        """
        
        individ_order = order.retrieve_single_order(id)
        if individ_order:
            return make_response(jsonify({
                "message" : "Ok",
                "order" : individ_order
            }), 200)
        else:
            response = {
                "message" : "Invalid id"
            }
            return make_response(jsonify(response), 400)

class UserOrders(Resource):
    """
    class for endpoint that restrieves all the orders made by a specific user
    """
    def get(self, id):
        user_orders = order.get_orders_by_user(id)
        if user_orders:
            return make_response(jsonify({
                "message" : "Ok",
                "orders by single user" : user_orders
            }), 200)
        else:
            response = {
                "message" : "Invalid user id"
            }
            return make_response(jsonify(response), 400)

class CancelParcel(Resource):
    """
    class for endpoint to cancel parcel order
    """
    def put(self, id):
        """
        PUT request to update parcel status to 'cancelled'
        """ 
        cancel_parcel = order.cancel_order(id)
        if cancel_parcel:
            return make_response(jsonify({
                "message" : "order is cancelled",
                "cancelled order" : cancel_parcel
            }), 201)
        else:
            return make_response(jsonify({
                    "message" : "Cancel failed. no order by that id"
                }), 400) 