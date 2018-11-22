import unittest
import json
#from app import create_app
#from ...api.v2.dbmodel import SenditDb as db
from app import create_app
from app.api.v2.dbmodel import SenditDb as db

class TestEdgeCases(unittest.TestCase):
    """
    class for testing invalid data fields while creating a new parcel
    """
    def setUp(self):
        """
        Initialize app and define test variables
        """
        self.test_app = create_app(config_option="TestConfig")
        self.app = self.test_app.test_client()
        self.test_app.testing = True
        self.blank_name = {
            "item" : "   ",
            "pickup" : "muranga",
            "dest" : "house",
            "pricing": "250",
            "user_id" : "12"
        }
        self.blank_pickup = {
            "item" : "A sack of potatoes",
            "pickup" : "  ",
            "dest" : "house",
            "pricing": "250",
            "user_id" : "12"
        }
        self.blank_dest = {
            "item" : "Two sacks of cherries",
            "pickup" : "muranga",
            "dest" : "  ",
            "pricing": "250",
            "user_id" : "12"
        }
        self.blank_pricing = {
            "item" : "Twenty pangas",
            "pickup" : "muranga",
            "dest" : "house",
            "pricing": "  ",
            "user_id" : "12"
        }
        self.blank_user = {
            "item" : "thirteen horses",
            "pickup" : "muranga",
            "dest" : "house",
            "pricing": "250",
            "user_id" : "  "
        }
    def tearDown(self):
        db.drop_all()

    def test_blank_item_name(self):
        response = self.app.post('/api/v2/parcels', data=json.dumps(self.blank_name), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid item name format', str(result))
    def test_blank_pickup_location_name(self):
        response = self.app.post('/api/v2/parcels', data=json.dumps(self.blank_pickup), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid pickup location name', str(result))
    def test_blank_destination(self):
        response = self.app.post('/api/v2/parcels', data=json.dumps(self.blank_dest), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid destination name', str(result))
    def test_blank_pricing(self):
        response = self.app.post('/api/v2/parcels', data=json.dumps(self.blank_pricing), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid price value', str(result))
    def test_blank_user_id(self):
        response = self.app.post('/api/v2/parcels', data=json.dumps(self.blank_user), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid user id', str(result))

  
if __name__ == "__main__":
    unittest.main()