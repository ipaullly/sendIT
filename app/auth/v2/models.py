from datetime import datetime, timedelta
from flask import current_app
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from app.api.v2.dbmodel import SenditDb

class User:
    """
    class to register user and generate tokens
    """
    def add_user(self, email, password):
        hashed_password = generate_password_hash(password)
        user_query = """INSERT INTO users (email, password) VALUES (%s, %s);"""
        tup = (email, hashed_password)
        SenditDb.add_to_db(user_query, tup)
        payload = {
            "email" : email,
            "hashed password" : hashed_password
        }
        return payload

"""
    def add_user(self):
    
        method to save a user's registration details
    
        setattr(self, 'id', db.user_no + 1)
        db.users.update({self.id: self})
        db.user_no += 1
        db.orders.update({self.id: {}})
        return self.lookup()
    
    def validate_password(self, password):
   
        method to validate user password

        if check_password_hash(self.password, password):
            return True
        return False
    
    def lookup(self):
        
        method to jsonify object that represents user
       
        keys = ['email', 'id']
        return {key: getattr(self, key) for key in keys}
    
    def generate_token(self, userID):
       
        method that generates token during each login
       
        try:
            payload = {
                'exp' : datetime.utcnow()+timedelta(minutes=5),
                'iat' : datetime.utcnow(),
                'id' : userID
            }
            token = jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
            return token
        except Exception as err:
            return str(err)

    @classmethod
    def get_user_by_email(cls, email):
        method for getting a user by email
    
        for user_id in db.users:
            user = db.users.get(user_id)
            if user.email == email:
                return user
        return None

"""