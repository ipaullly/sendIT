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
        author = data['username']

        try:
            if "  " in item:
                raise Exception
            elif type(pricing) is not int:
                raise Exception
            else:
                order.create_order(item, pickup, dest, pricing, author)
                return make_response(jsonify({
                    "message" : "delivery order created successfully"
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
        single = order.retrieve_single_order(id)
        return make_response(jsonify({
            "message" : "Ok",
            "order" : single
        }), 200)

class UserOrders(Resource):
    """
    class for endpoint that restrieves all the orders made by a specific user
    """
    def get(self, id):
        user_orders = order.get_orders_by_user(id)
        return make_response(jsonify({
            "message" : "Ok",
            "orders by single user" : user_orders
        }), 200)

class CancelParcel(Resource):
    """
    class for endpoint to cancel parcel order
    """
    def put(self, id):
        """
        PUT request to update parcel status to 'cancelled'
        """
        cancel_parcel = order.cancel_order(id)
        return make_response(jsonify({
            "message" : "order is cancelled",
            "cancelled order" : cancel_parcel
        }), 201)
            