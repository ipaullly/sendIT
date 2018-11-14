from ... import create_app
import unittest
import json

class TestEdgeCases(unittest.TestCase):
    """
    class for testing invalid input data and 
    """
    def setUp(self):
        """
        Initialize app and define test variables
        """
        create_app().testing = True
        self.app = create_app().test_client()
        self.dummy = {
            "item" : "  ",
            "pickup" : "muranga",
            "dest" : "house",
            "pricing": 250,
            "user_id" : "12"
        }
        self.invalid_registration_details = {
            "email" : "   ",
            "password" : "ghfgfg"
        }

    def test_empty_strings_in_POST_create_order(self):
        """
        Test whether API can create a new delivery order via POSt request
        """
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.dummy), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('wrong input format', str(result))
    
    def test_whitespces_in_email_field(self):
        response2 = self.app.post('/auth/v1/register', data=json.dumps(self.invalid_registration_details), content_type='application/json')
        self.assertEqual(response2.status_code, 400)
        res = json.loads(response2.data)
        self.assertEqual("{'message': 'Whitespaces are invalid inputs'}", str(res))
    
if __name__ == "__main__":
    unittest.main()