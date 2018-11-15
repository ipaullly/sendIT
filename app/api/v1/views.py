from flask_restful import Resource
from flask import make_response, jsonify, request
from .models import Parcels

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

        try:
            if "  " in item:
                raise Exception
            elif type(pricing) is not int:
                raise Exception
            else:
                res = order.create_order(item, pickup, dest, pricing, author)
                return make_response(jsonify({
                    "message" : "delivery order created successfully",
                    "new delivery order" : res
                }), 201)
        except Exception:
            return make_response(jsonify({
                "message" : "wrong input format"
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
        
        single = order.validate_ID(id)
        if single:
            individ_order = order.retrieve_single_order(id)
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
        if order.validate_ID(id):
            user_orders = order.get_orders_by_user(id)
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
        try:
            check_id = order.validate_ID(id)
            if not check_id:
                raise Exception  
            else:
                cancel_parcel = order.cancel_order(check_id)
                return make_response(jsonify({
                    "message" : "order is cancelled",
                    "cancelled order" : cancel_parcel
                }), 201)
        except Exception:
            return make_response(jsonify({
                    "message" : "Cancel failed. no order by that id"
                }), 400) 