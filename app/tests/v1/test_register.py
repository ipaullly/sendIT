from ... import create_app
import unittest
import json

class AuthTestCase(unittest.TestCase):
    """
    test class for the registration endpoint
    """
    def setUp(self):
        create_app().testing = True
        self.app = create_app().test_client()
        self.mock_data = {
            'email' : 'test@hotmail.com',
            'password' : 'holy_water'
        }
        self.mock_data2 = {
            'email' : 'qarth@hotmail.com',
            'password' : 'jade_sea'
        }
          
    
    def test_signup(self):
        response2 = self.app.post('/auth/v1/register', data=json.dumps(self.mock_data), content_type='application/json')
        res = json.loads(response2.data)
        self.assertEqual("{'message': 'you have successfully registered an account'}", str(res))


    def test_if_registered(self):
        response1 = self.app.post('/auth/v1/register', data=json.dumps(self.mock_data2), content_type='application/json')
        self.assertEqual(response1.status_code, 201)
        duplicate_signup = self.app.post('/auth/v1/register', data=json.dumps(self.mock_data2), content_type='application/json')
        self.assertEqual(duplicate_signup.status_code, 409)
        res = json.loads(duplicate_signup.data)
        self.assertIn('Account with provided email exists. please login', str(res))

if __name__ == "__main__":
    unittest.main()