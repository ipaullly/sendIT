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
        
        if not new_user:
            response = {
                'message' : 'User with the email already exists'
            }
            return make_response(jsonify(response), 400)


        return make_response(jsonify({
            'message' : 'you have successfully registered an account',
            'data' : new_user
        }), 201)

class SignIn(Resource):
    """
    class that handles logging into user accounts and token generation
    """
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        
        queried_user = user.get_user_by_email(email)

        if not queried_user:
            response = {
                'message' : 'No user by that email exists. please enter information again'
            }
            return make_response(jsonify(response), 401)
        
        user_id = queried_user[0]['id']
        check_password = user.validate_password(password, email)
        if not check_password:
            response = {
                'message' : 'incorrect password. please enter again'
            }
            return make_response(jsonify(response), 401)
        auth_token = user.generate_token(user_id)
        if not auth_token:
            response = {
                'message' : 'token generation failed'
            }
            return make_response(jsonify(response), 401)
        response = {
            'message' : 'Successfully logged in',
            'data' : auth_token
        }
        return make_response(jsonify(response), 200)
      