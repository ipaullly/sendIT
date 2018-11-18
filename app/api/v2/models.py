from ...db_config import init_db

class OrderParcel:
    """
    model for performing CRUD on orders table in the database
    """
    def __init__(self):
        self.db = init_db()
    
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
        , pricing, user_id) VALUES (%(item_name)s, %(pickup_location)s, \
        %(destination)s, %(pricing)s, %(user_id)s)"""
        curr = self.db.cursor()
        curr.execute(query, payload)
        self.db.commit()
        return payload

  