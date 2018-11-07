from flask_restful import Resource
from flask import make_response,jsonify, request
from .models import User

class Registration(Resource):
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']

        new_user = User(email=email, password=password)
        new_user.add_user()
        
        return make_response(jsonify({
            'message' : 'you have successfully registered an account'
        }), 201)