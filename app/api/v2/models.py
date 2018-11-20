import os
from .dbmodel import SenditDb

uri = os.getenv('DEV_DB_URI')
SenditDb.start_db(uri)

class OrderParcel:
    """
    model for performing CRUD on orders table in the database
    """
    def create_order(self, item, pickup, dest, pricing, user_id):
        """
        instance method to generate new entry into delivery orders list
        """
        payload = {
            "item_name" : item,
            "pickup_location" : pickup,
            "destination" : dest,
            "pricing" : pricing,
            "user_id" : user_id
        }
        query = """INSERT INTO orders (item_name, pickup_location, destination \
        , pricing, user_id) VALUES (%s, %s, %s, %s, %s)"""
        tup = (item, pickup, dest, pricing, user_id)
        SenditDb.add_to_db(query, tup)
        
        return payload

    def order_list(self):
        """
        retrieves entire list of delivery orders
        """
        query = """SELECT item_name, pickup_location, destination FROM orders"""
        resp = SenditDb.retrieve_all(query)
        return resp
    
    