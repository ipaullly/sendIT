from ... import create_app
import unittest
import json

class LoginTestCase(unittest.TestCase):
    """
    test class for the registration endpoint
    """
    def setUp(self):
        create_app().testing = True
        self.app = create_app().test_client()
        self.mock_data = {
            'email' : 'test@chocoly.com',
            'password' : 'balerion'
        }
        self.not_user_data = {
            'email' : 'not_user@chocoly.com',
            'password' : 'silmarillion'
        }

    def test_user_signin(self):
        #test if a registered user can log in
        res = self.app.post('/auth/v1/register', data=json.dumps(self.mock_data), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        signin_res = self.app.post('/auth/v1/login', data=json.dumps(self.mock_data), content_type='application/json')
        result = json.loads(signin_res.data)
        self.assertIn('Successfully logged in', str(result))
        self.assertEqual(signin_res.status_code, 200)
        self.assertTrue(result)

    def test_non_registered_user(self):
        #test that unregistered user cannot log in
        res = self.app.post('/auth/v1/login', data=json.dumps(self.mock_data), content_type='application/json')
        result = json.loads(res.data)
        self.assertIn("{'message': 'wrong input format, please enter details again'}", str(result))
        self.assertEqual(res.status_code, 500)


if __name__ == "__main__":
    unittest.main()
        