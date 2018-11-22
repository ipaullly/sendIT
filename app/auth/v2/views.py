from flask_restful import Resource
from flask import make_response,jsonify, request
from app.auth.v2.models import User
from app.utilities.validation_functions import check_for_space, check_email_format, check_password_strength

user = User()

class SignUp(Resource):
    """
    class that handles registration of new user
    """
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        

        if not check_for_space(email):
            response = {
                'message' : 'Whitespaces are invalid inputs'
            }
            return make_response(jsonify(response), 400)
   
        if not check_email_format(email):
            response = {
                'message' : 'Invalid email format'
            }
            return make_response(jsonify(response), 400)

        if not check_password_strength(password):
            response = {
                'message' : 'Ensure your password is at least 8 charaters and includes an Uppercase letter'
            }
            return make_response(jsonify(response), 400)
        
        new_user = user.add_user(email, password)
        
        return make_response(jsonify({
            'message' : 'you have successfully registered an account',
            'data' : new_user
        }), 201)
        