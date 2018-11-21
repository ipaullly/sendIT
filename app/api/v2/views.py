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
        status = "pending"
        current_location = "sendIT HQ"

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


        res = order.create_order(item, pickup, dest, pricing, author, status, current_location)

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
            return make_response(jsonify({
                "message" : "ok",
                "data" : resp
            }), 200)
        return make_response(jsonify({
                "message" : "No orders in the database"
            }), 400) 


class ParcelDestination(Resource):
    """
    class for endpoint to allow user to update order destination
    """
    def put(self, id):
        """
        PUT request to update parcel status to 'cancelled'
        """ 
        new_destination = request.get_json()['new_destination']

        if not check_for_space(new_destination):
            return make_response(jsonify({
                "message" : "Invalid destination value"
            }), 400)

    
        updated_parcel = order.update_destination(new_destination, id)
        if updated_parcel:
            return make_response(jsonify({
                "message" : "New destination updated",
                "data" : updated_parcel
            }), 201)
        else:
            return make_response(jsonify({
                    "message" : "Destination update failed. no order by that id"
                }), 400) 

class ParcelStatus(Resource):
    """
    class for endpoint to cancel parcel order
    """
    def put(self, id):
        """
        PUT request to update parcel status to
        """ 
        order_status = request.get_json()['status']
        
        if order_status == 'In transit' or order_status == 'Arrived':
            
            order_status = order.update_order_status(order_status, id)
            if order_status:
                return make_response(jsonify({
                    "message" : "Success",
                    "data" : order_status
                }), 201)
            else:
                return make_response(jsonify({
                        "message" : "Update of order status failed. no order by that id"
                    }), 400)
        else:
            return make_response(jsonify({
                    "message" : "Status entered is invalid"
                }), 400) 
    
class ParcelCurrentLocation(Resource):
    """
    class for endpoint to cancel parcel order
    """
    def put(self, id):
        """
        PUT request to update parcel status to
        """ 
        order_location = request.get_json()['current_location']
        
        new_location = order.update_current_location(order_location, id)
        if new_location:
            return make_response(jsonify({
                "message" : "Success",
                "data" : new_location
            }), 201)
        else:
            return make_response(jsonify({
                "message" : "Update of current order failed. no order by that id"
            }), 400)
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
                "message" : "order is cancelled"
            }), 201)
        else:
            return make_response(jsonify({
                    "message" : "Cancel failed. no order by that id"
                }), 400) 

class UserOrders(Resource):
    """
    class for endpoint that restrieves all the orders made by a specific user
    """
    def get(self, id):
        user_orders = order.get_orders_by_user(id)
        if user_orders:
            return make_response(jsonify({
                "message" : "Ok",
                "data" : user_orders
            }), 200)
        else:
            response = {
                "message" : "Invalid user id"
            }
            return make_response(jsonify(response), 400)