from ... import create_app
import unittest
import json

class TestPracelCreation(unittest.TestCase):
    """
    class for Parcels test case
    """
    def setUp(self):
        """
        Initialize app and define test variables
        """
        create_app().testing = True
        self.app = create_app().test_client()
        self.data = {
            "item" : "seven ballons",
            "pickup" : "Biashara street",
            "dest" : "Kikuyu town",
            "pricing": "250 ksh"
        }

    def test_POST_create_delivery_order(self):
        """
        Test whether API can create a new delivery order via POSt request
        """
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('delivery order created', str(result))
    
    def test_GET_delivery_orders_list(self):
        """
        Test if API can retrieve a list of delivery orders
        """
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.get('/api/v1/parcels', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertIn('seven ballons', str(result))
    
    def test_GET_single_delivery_order(self):
        """
        Test if API can retrieve a single delivery order by its id
        """
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        result = self.app.get('/api/v1/parcels/1')
        self.assertEqual(result.status_code, 200)
        self.assertIn('seven ballons', str(result.data))

    def test_PUT_cancel_delivery_order(self):
        """
        Test if API can cancel order by changing order status
        """
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        result = self.app.put('/api/v1/parcels/1/cancel')
        self.assertEqual(result.status_code, 201)
        self.assertIn('order is cancelled', str(result.data))
        
# make the tests you have written executable

if __name__ == "__main__":
    unittest.main()