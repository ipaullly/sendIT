from .. import create_app
import unittest
import json

class TestPracelCreation(unittest.TestCase):
    def setUp(self):
        create_app().testing = True
        self.app = create_app().test_client()
        self.data = {
            "item" : "seven ballons",
            "pickup" : "Biashara street",
            "dest" : "Kikuyu town",
            "pricing": "250 ksh"
        }

    def test_POST_create_delivery_order(self):
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('seven ballons', str(result))
    
    def test_GET_delivery_orders_list(self):
        """Test if API can retrieve a list of delivery orders"""
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.get('/api/v1/parcels', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertIn('seven ballons', str(result))


# make the tests you have written executable

if __name__ == "__main__":
    unittest.main()