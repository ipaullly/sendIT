import unittest
import json
from ... import create_app
from ...api.v2.dbmodel import SenditDb

class TestEdgeCases(unittest.TestCase):
    """
    class for testing invalid input data and 
    """
    def setUp(self):
        """
        Initialize app and define test variables
        """
        test_app = create_app(config_option="TestConfig")
        test_app.testing = True
        self.app = test_app().test_client()
        self.dummy = {
            "item" : "  ",
            "pickup" : "muranga",
            "dest" : "house",
            "pricing": "250",
            "user_id" : "12"
        }
        self.blank_email = {
            "email" : "   ",
            "password" : "ghfgfg"
        }
        self.invalid_pattern = {
            "email" : "house",
            "password" : "xgss"
        }
        self.invalid_id = {
            "item" : "seven ballons",
            "pickup" : "Biashara street",
            "dest" : "Kikuyu town",
            "pricing": "250",
            "user_id" : "12"
        }
        self.weak_password = {
            "email" : "house@gmail.org",
            "password" : "nnnibal"
        }
    
    def tearDown(self):
        SenditDb.drop_all


    def test_empty_strings_in_POST_create_order(self):
        """
        Test whether API can create a new delivery order via POSt request
        """
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.dummy), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid item name format', str(result))
    
    def test_whitespces_in_email_field(self):
        response2 = self.app.post('/auth/v1/register', data=json.dumps(self.blank_email), content_type='application/json')
        self.assertEqual(response2.status_code, 400)
        res = json.loads(response2.data)
        self.assertEqual("{'message': 'Whitespaces are invalid inputs'}", str(res))

    def test_wrong_email_pattern(self):
        response3 = self.app.post('/auth/v1/register', data=json.dumps(self.invalid_pattern), content_type='application/json')
        self.assertEqual(response3.status_code, 400)
        res = json.loads(response3.data)
        self.assertEqual("{'message': 'Invalid email format'}", str(res))
    
    def test_invalid_parcel_id(self):
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.invalid_id), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        resul = self.app.get('/api/v1/parcels/30')
        self.assertEqual(resul.status_code, 400)
      #  self.assertIn('b\'{"message":"Invalid id"}\\n\'', str(resul.data))
    
    def test_invalidID_cancel_order(self):
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.invalid_id), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        result = self.app.put('/api/v1/parcels/30/cancel')
        self.assertEqual(result.status_code, 400)
       # self.assertIn('{"message": "Cancel failed. no order by that id"}', str(result.data))
    def test_weak_password(self):
        respon = self.app.post('/auth/v1/register', data=json.dumps(self.weak_password), content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        res = json.loads(respon.data)
        self.assertEqual("{'message': 'Ensure your password is at least 8 charaters and includes an Uppercase letter'}", str(res))

if __name__ == "__main__":
    unittest.main()