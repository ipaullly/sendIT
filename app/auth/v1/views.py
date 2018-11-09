from flask_restful import Resource
from flask import make_response,jsonify, request
from .models import User

class Registration(Resource):
    """
    class that handles registration of new user
    """
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
        
class SignIn(Resource):
    """
    class that handles logging into user accounts and token generation
    """
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        try:
            user = User.get_user_by_email(email)
            user_id = user.id
            if user and user.validate_password(password):
                auth_token = user.generate_token(user_id)
                if auth_token:
                    response = {
                        'message' : 'Successfully logged in and token generated'
                    }
                    return make_response(jsonify(response), 200)
            else:
                response = {
                    'message' : 'User with email already exists, please login'
                }
                return make_response(jsonify(response), 401)
        except Exception as err:
            response = {
                'message' : str(err)
            }
            return make_response(jsonify(response), 500)