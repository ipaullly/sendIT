from flask_restful import Resource
from flask import make_response,jsonify, request
from .models import User
from ...utilities.validation_functions import check_for_space, check_email_format, check_password_strength

class Registration(Resource):
    """
    class that handles registration of new user
    """
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        
        if check_for_space(email):
            if check_email_format(email):
                if check_password_strength(password):
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
                        return make_response(jsonify(response), 409)
                else:
                    response = {
                        'message' : 'Ensure your password is at least 8 charaters and includes an Uppercase letter'
                    }
                    return make_response(jsonify(response), 400)
            else:
                response = {
                    'message' : 'Invalid email format'
                }
                return make_response(jsonify(response), 400)
        else:
            response = {
                'message' : 'Whitespaces are invalid inputs'
            }
            return make_response(jsonify(response), 400)

        
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
                        'message' : 'Successfully logged in'
                    }
                    return make_response(jsonify(response), 200)
            else:
                response = {
                    'message' : 'Invalid password, please enter it again'
                }
                return make_response(jsonify(response), 401)
        except Exception:
            response = {
                'message' : 'wrong email format, please enter email again'
            }
            return make_response(jsonify(response), 400)