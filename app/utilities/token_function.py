import os
import jwt

def decode_token(token):
    """
    function to retrieve authentication privileges from request header
    """
    try:
        #attempt to decode token using SECRET_KEY variable
        payload = jwt.decode(token, os.environ.get('SECRET_KEY'))
        return payload['id']
    except  jwt.ExpiredSignatureError:
        # expired token returns an error string
        return "Token expired. please login again to generate fresh token"
    except jwt.InvalidTokenError:
        #the token is not valid, throw error
        return "Unworthy token. Please login to get fresh authorization"

