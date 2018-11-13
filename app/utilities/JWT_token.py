from flask import current_app
import jwt


def decode_token(token):
    """
    method to decode the token generated during login
    """
    try:
        #attempt to decode token using SECRET_KEY variable
        payload = jwt.decode(token, current_app.config.get('SECRET_KEY'))
        return payload['id']
    except  jwt.ExpiredSignatureError:
        # expired token returns an error string
        return "Token expired. please login again to generate fresh token"
    except jwt.InvalidTokenError:
        #the token is not valid, throw error
        return "Unworthy token. Please login to get fresh authorization"