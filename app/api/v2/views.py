from flask_restful import Resource
from flask import make_response, jsonify, request
from ...utilities.validation_functions import check_for_space
from .models import OrderParcel

order = OrderParcel()

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
        if resp:
            return jsonify(resp)
        return jsonify({"message" : "No orders in the database"})

class CancelParcel(Resource):
    """
    User endpoint to update delivery order destination
    """
    def put(self, id):
        """
        PUT request to update parcel destination to 'cancelled'
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