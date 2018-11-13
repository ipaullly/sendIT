from datetime import datetime, timedelta
from flask import current_app
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

class MockDb():
    """
    class for a data structure database
    """
    def __init__(self):
        self.users = {}
        self.orders = {}
        self.user_no = 0
        self.entry_no = 0
    def drop(self):
        self.__init__()

db = MockDb()

class Parent():
    """
    user class will inherit this class
    """
    def update(self, data):
        # Validate the contents before passing to mock database
        for key in data:
            setattr(self, key, data[key])
        setattr(self, 'last_updated', datetime.utcnow().isoformat())
        return self.lookup()

class User(Parent):
    """
    class to register user and generate tokens
    """
    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)
        self.id = None
        self.created_at = datetime.utcnow().isoformat()
        self.last_updated = datetime.utcnow().isoformat()

    def add_user(self):
        """
        method to save a user's registration details
        """
        setattr(self, 'id', db.user_no + 1)
        db.users.update({self.id: self})
        db.user_no += 1
        db.orders.update({self.id: {}})
        return self.lookup()
    
    def validate_password(self, password):
        """
        method to validate user password
        """
        if check_password_hash(self.password, password):
            return True
        return False
    
    def lookup(self):
        """
        method to jsonify object that represents user
        """
        keys = ['email', 'id']
        return {key: getattr(self, key) for key in keys}
    
    def generate_token(self, userID):
        """
        method that generates token during each login
        """
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
        """
        method for getting a user by email
        """
        for user_id in db.users:
            user = db.users.get(user_id)
            if user.email == email:
                return user
        return None