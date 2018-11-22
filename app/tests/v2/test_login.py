import unittest
import json
#from ... import create_app
#from ...api.v2.dbmodel import SenditDb
from app import create_app
from app.api.v2.dbmodel import SenditDb

class LoginTestCase(unittest.TestCase):
    """
    test class for the registration endpoint
    """
    def setUp(self):
        self.test_app = create_app(config_option="TestConfig")
        self.app = self.test_app.test_client()
        self.test_app.testing = True
        self.mock_data = {
            'email' : 'test@chocoly.com',
            'password' : 'Balerion'
        }
        self.not_user_data = {
            'email' : 'not_user@chocoly.com',
            'password' : 'silmarillion'
        }

    def test_user_signin(self):
        #test if a registered user can log in
        res = self.app.post('/auth/v2/register', data=json.dumps(self.mock_data), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        signin_res = self.app.post('/auth/v2/login', data=json.dumps(self.mock_data), content_type='application/json')
        result = json.loads(signin_res.data)
        self.assertIn('Successfully logged in', str(result))
        self.assertEqual(signin_res.status_code, 200)
        self.assertTrue(result)

    def test_non_registered_user(self):
        #test that unregistered user cannot log in
        res = self.app.post('/auth/v2/login', data=json.dumps(self.mock_data), content_type='application/json')
        result = json.loads(res.data)
        self.assertIn("{'message': 'wrong email format, please enter email again'}", str(result))
        self.assertEqual(res.status_code, 400)

    def tearDown(self):
        SenditDb.drop_all()

if __name__ == "__main__":
    unittest.main()
        