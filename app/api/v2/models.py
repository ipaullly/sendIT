from .dbmodel import SenditDb

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

        input_query = """INSERT INTO orders (item_name, pickup_location, destination \
        , pricing, user_id) VALUES (%s, %s, %s, %s, %s);"""
        tup = (item, pickup, dest, pricing, user_id)
        SenditDb.add_to_db(input_query, tup)
        
        return payload

    def order_list(self):
        """
        retrieves entire list of delivery orders
        """
        query = """SELECT item_name, pickup_location, destination FROM orders;"""
        resp = SenditDb.retrieve_all(query)
        return resp
    
    def update_destination(self, new_dest, parcel_id):
        """
        updates the destination of a user's parcels
        """
        payload = {
            "updated_destination" : new_dest
        }
        input_query = """SELECT destination FROM orders WHERE order_id={}""".format(parcel_id)
        response = SenditDb.retrieve_one(input_query)
        if not response:
            return False
        update_query = """UPDATE orders SET destination = '{}' WHERE order_id={}""".format(new_dest, parcel_id)
        SenditDb.update_row(update_query)
        return payload

    def update_order_status(self, status, parcel_id):
        """
        updates the status of the parcel delivery order
        """
        payload = {
            "order status" : status
        }
        input_query = """SELECT * FROM orders WHERE order_id={}""".format(parcel_id)
        response = SenditDb.retrieve_one(input_query)
        if not response:
            return False
        status_query = """UPDATE orders SET status = '{}' WHERE order_id={}""".format(status, parcel_id)
        SenditDb.update_row(status_query)
        return payload

    def update_current_location(self, new_location, parcel_id):
        """
        updates the current location of the parcel delivery order
        """
        payload = {
            "Updated location" : new_location
        }
        input_query = """SELECT * FROM orders WHERE order_id={}""".format(parcel_id)
        response = SenditDb.retrieve_one(input_query)
        if not response:
            return False
        status_query = """UPDATE orders SET current_location = '{}' WHERE order_id={}""".format(new_location, parcel_id)
        SenditDb.update_row(status_query)
        return payload

    def cancel_order(self, parcel_id):
        """
        cancels a parcel delivery order by id
        """
        input_query = """SELECT * FROM orders WHERE order_id={}""".format(parcel_id)
        response = SenditDb.retrieve_one(input_query)
        if not response:
            return False
        status_query = """UPDATE orders SET status = 'cancelled' WHERE order_id={}""".format(parcel_id)
        SenditDb.update_row(status_query)
        return True

    def get_orders_by_user(self, user_id):
        """
        retrieves a list of parcels by user id
        """
        input_query = """SELECT order_id, item_name, destination, status, \
         current_location FROM orders WHERE user_id={}""".format(user_id)
        response = SenditDb.retrieve_all(input_query)
        if not response:
            return False
        payload = {
            "user orders" : response
        }
        return payload