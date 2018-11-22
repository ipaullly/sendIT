import os
from datetime import datetime, timedelta
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from app.api.v2.dbmodel import SenditDb

#secret_key = os.environ.get('SECRET_KEY')

class User:
    """
    class to register user and generate tokens
    """
    def add_user(self, email, password):
        hashed_password = generate_password_hash(password)
        email_query = """SELECT * FROM users WHERE email = '{}'""".format(email)
        duplicate_email = SenditDb.retrieve_all(email_query)
        if duplicate_email:
            return False
        user_query = """INSERT INTO users (email, password) VALUES (%s, %s) RETURNING email, id"""
        tup = (email, hashed_password)
        resp = SenditDb.add_to_db(user_query, tup)
        payload = resp
        return payload
 
    def get_user_by_email(self, email):
        email_query = """SELECT * FROM users WHERE email = '{}'""".format(email)
        response = SenditDb.retrieve_all(email_query)
        if not response:
            return False
        return response
        

    def validate_password(self, password, user_email):
        query = """SELECT password FROM users WHERE email='{}'""".format(user_email)
        result = SenditDb.retrieve_one(query)

        if not check_password_hash(result['password'], password):
            return False
        return True

    
    def generate_token(self, userID):
       
        try:
            payload = {
                'exp' : datetime.utcnow()+timedelta(minutes=2),
                'iat' : datetime.utcnow(),
                'id' : userID
            }
            token = jwt.encode(
                payload,
                os.environ.get('SECRET_KEY'),
                algorithm='HS256'
            )
            return token
        except Exception as err:
            return str(err)
    

