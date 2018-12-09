import unittest
import json
#from ... import create_app
#from ...api.v2.dbmodel import SenditDb
from app import create_app
from app.api.v2.dbmodel import SenditDb

class AuthTestCase(unittest.TestCase):
    """
    test class for the registration endpoint
    """
    def setUp(self):
        self.test_app = create_app(config_option="TestConfig")
        self.app = self.test_app.test_client()
        self.test_app.testing = True
        self.mock_data = {
            'email' : 'test@hotmail.com',
            'password' : 'Goriguty'
        }
        self.mock_data2 = {
            'email' : 'qarth@hotmail.com',
            'password' : 'Hannniabl'
        }
    
    def tearDown(self):
        SenditDb.drop_all()
          
    
    def test_signup(self):
        response2 = self.app.post('/auth/v2/signup', data=json.dumps(self.mock_data), content_type='application/json')
        res = json.loads(response2.data)
        self.assertEqual("{'message': 'you have successfully registered an account'}", str(res))


    def test_if_registered(self):
        response1 = self.app.post('/auth/v2/signup', data=json.dumps(self.mock_data2), content_type='application/json')
        self.assertEqual(response1.status_code, 201)
        duplicate_signup = self.app.post('/auth/v2/signup', data=json.dumps(self.mock_data2), content_type='application/json')
        self.assertEqual(duplicate_signup.status_code, 409)
        res = json.loads(duplicate_signup.data)
        self.assertIn('Account with provided email exists. please login', str(res))

if __name__ == "__main__":
    unittest.main()