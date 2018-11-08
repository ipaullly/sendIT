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
    
    def test_signup(self):
        response = self.app.post('/auth/v1/register', data=json.dumps(self.mock_data), content_type='application/json')
        res = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(res['message'], "you have successfully registered an account")




if __name__ == "__main__":
    unittest.main()