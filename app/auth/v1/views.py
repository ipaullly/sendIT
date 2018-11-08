from flask_restful import Resource
from flask import make_response,jsonify, request
from .models import User

class Registration(Resource):
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']

        if not User.get_user_by_email(email):
            new_user = User(email=email, password=password)
            new_user.add_user()
        
            return make_response(jsonify({
                'message' : 'you have successfully registered an account'
            }), 201)
        else:
            response = {
                'message': 'Account with provided email exists. please login'
            }

            return make_response((jsonify(response)), 202)