from flask_restful import Resource
from flask import make_response, jsonify, request
from .models import Parcels


class ParcelList(Resource, Parcels):

    def __init__(self):
        self.order = Parcels()

    def post(self):
        data = request.get_json()
        item = data['item']
        pickup = data['pickup']
        dest = data['dest']
        pricing = data['pricing']

        self.order.create_order(item, pickup, dest, pricing)

        return make_response(jsonify({
            "message" : "delivery order created successfully"
        }), 201)
    
    def get(self):
        pass

class IndividualParcel(Resource):

    def get(self, id):
        pass

    def put(self, id):
        pass