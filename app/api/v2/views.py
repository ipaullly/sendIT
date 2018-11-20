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

        if not check_for_space(item):
           return make_response(jsonify({
                "message" : "Invalid item name format"
            }), 400)

        if not check_for_space(pickup):
            return make_response(jsonify({
                "message" : "Invalid pickup location name"
            }), 400)

        if not check_for_space(dest):
            return make_response(jsonify({
                "message" : "Invalid destination name"
            }), 400) 

        if not check_for_space(pricing):
            return make_response(jsonify({
                "message" : "Invalid price value"
            }), 400)


        if not check_for_space(author):
            return make_response(jsonify({
                "message" : "Invalid user id"
            }), 400) 

        res = order.create_order(item, pickup, dest, pricing, author)

        if res == "User already ordered this item":
            return make_response(jsonify({
                "message" : res
            }), 409)

        return make_response(jsonify({
            "message" : "delivery order created successfully",
            "data" : res
        }), 201)
    
    def get(self):
        """
        get method to retrieve list of all orders
        """
        resp = order.order_list()
        if resp:
            return jsonify(resp)
        return jsonify({"message" : "No orders in the database"})


class SingleParcel(Resource):
    """
    class for endpoint to allow user to update order destination
    """
    def put(self, id):
        """
        PUT request to update parcel status to 'cancelled'
        """ 
        new_destination = request.get_json()['new_destination']
        item_id = request.get_json()['item_id']
    
        updated_parcel = order.update_destination(new_destination, item_id)
        if updated_parcel:
            return make_response(jsonify({
                "message" : "New destination updated",
                "data" : updated_parcel
            }), 201)
        else:
            return make_response(jsonify({
                    "message" : "Destination update failed. no order by that id"
                }), 400) 