import codecs
from flask_restful import Resource
from flask import make_response,jsonify, request
#from ...auth.v2.models import User
#from ...utilities.validation_functions import check_for_space, check_email_format, check_password_strength
from app.auth.v2.models import User
from app.utilities.validation_functions import check_for_space, check_email_format, check_password_strength

user = User()

class SignUp(Resource):
    """
    class that handles registration of new user
    """
    def post(self):
        
        try:
            data = request.get_json()
            password = data['password']
            email = data['email']
        except Exception:
            response = {
                'message' : 'Invalid key field'
            }
            return make_response(jsonify(response), 400)

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

        checked_email = user.check_duplicate_email(email)
        if checked_email:
            response = {
                'message' : 'User with the email already exists'
            }
            return make_response(jsonify(response), 400)
            
        role = user.check_role()
        
        if role:
            user_role = "user"
        if not role:
            user_role = "admin"

        new_user = user.add_user(email, password, user_role)
        
        return make_response(jsonify({
            'message' : 'you have successfully registered an account',
            'data' : new_user
        }), 201)

class SignIn(Resource):
    """
    class that handles logging into user accounts and token generation
    """
    def post(self):
        try:
            data = request.get_json()
            email = data['email']
            password = data['password']
        except Exception:
            response = {
                'message' : 'Invalid key field'
            }
            return make_response(jsonify(response), 400)
        queried_user = user.get_user_by_email(email)

        if not check_email_format(email):
            response = {
                'message' : 'Invalid email. please check the format'
            }
            return make_response(jsonify(response), 400)

        if not queried_user:
            response = {
                'message' : 'incorrect login credentials. please enter details again'
            }
            return make_response(jsonify(response), 401)
        
        user_id = queried_user[0]['id']
        check_password = user.validate_password(password, email)
        if not check_password:
            response = {
                'message' : 'incorrect login credentials. please enter details again'
            }
            return make_response(jsonify(response), 401)
        
        auth_token = user.generate_token(user_id)
        
        if not auth_token:
            response = {
                'message' : 'token generation failed'
            }
            return make_response(jsonify(response), 401)
        
        #str_token = str(object=auth_token, encoding='utf-8', errors='strict')
        #str_token = auth_token.encode()

        response = {
            'message' : 'Successfully logged in',
            'data' : str(auth_token, 'utf-8')
        }
        return make_response(jsonify(response), 200)
      