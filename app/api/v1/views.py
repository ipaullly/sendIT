from flask_restful import Resource
from flask import make_response, jsonify, request
from .models import Parcels

order = Parcels()

class ParcelList(Resource):

    def post(self):
        data = request.get_json()
        item = data['item']
        pickup = data['pickup']
        dest = data['dest']
        pricing = data['pricing']

        order.create_order(item, pickup, dest, pricing)
        orders = order.db
        return make_response(jsonify({
            "message" : "delivery order created successfully",
            "orders" : orders
        }), 201)
    
    def get(self):
        resp = order.order_list()
        return make_response(jsonify({
            "message" : "ok",
            "Delivery Orders" : resp
        }), 200)


class IndividualParcel(Resource):

    def get(self, id):
        single = order.retrieve_single_order(id)
        return make_response(jsonify({
            "message" : "Ok",
            "order" : single
        }), 200)


    def put(self, id):
        pass
            