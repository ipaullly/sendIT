import os
from datetime import datetime, timedelta
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
#from ...api.v2.dbmodel import SenditDb

from app.api.v2.dbmodel import SenditDb

#secret_key = os.environ.get('SECRET_KEY')

class User:
    """
    class to register user and generate tokens
    """
    def add_user(self, email, password, role):
        hashed_password = generate_password_hash(password)
        
        user_query = """INSERT INTO users (email, password, role) VALUES (%s, %s, %s) RETURNING email, role, id"""
        tup = (email, hashed_password, role)
        resp = SenditDb.insert_fetch_from_db(user_query, tup)
        payload = resp
        return payload

    def check_duplicate_email(self, email):

        email_query = """SELECT * FROM users WHERE email = '{}'""".format(email)
        duplicate_email = SenditDb.retrieve_all(email_query)
        if duplicate_email:
            return True

    def check_admin(self, user_id):
        """
        method checks whether a user is an admin by id
        """
        admin_query = """SELECT role FROM users WHERE id = {}""".format(user_id)
        user_role = SenditDb.retrieve_all(admin_query)
        if user_role[0]['role'] == 'admin':
            return True

    def check_role(self):
        """
        method returns True if an account with admin privileges already exists in the database
        """
        role_query = """SELECT role FROM users ORDER BY id ASC;"""
        user_roles = SenditDb.retrieve_all(role_query)
        print(user_roles)
        for role in user_roles:
            if role['role'] == 'admin':
                return True
 
    def get_user_by_email(self, email):
        email_query = """SELECT * FROM users WHERE email = '{}'""".format(email)
        response = SenditDb.retrieve_all(email_query)
        if not response:
            return False
        return response
    
    def get_email_by_id(self, id):
        query = """SELECT email FROM users WHERE id = '{}'""".format(id)
        response = SenditDb.retrieve_all(query)
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
                'exp' : datetime.utcnow()+timedelta(minutes=60),
                'iat' : datetime.utcnow(),
                'id' : userID
            }
            token = jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm='HS256').decode('utf-8')
            return token
        except Exception as err:
            return str(err)
    

