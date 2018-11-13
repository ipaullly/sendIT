
parcels = []

class Parcels:
    """
    Class with CRUD functionalities on the Parcels resource
    """
    def __init__(self):
        self.db = parcels
        self.parcel_status = 'pending'

    def create_order(self, item, pickup, dest, pricing, username):
        """
        instance method to generate new entry into delivery orders list
        """
        payload = {
            "id" : len(self.db) + 1,
            "itemName" : item,
            "pickupLocation" : pickup,
            "destination" : dest,
            "pricing" : pricing,
            "authorId" : username,
            "status" : self.parcel_status
        }
        self.db.append(payload)

    def order_list(self):
        """
        retrieves entire list of delivery orders
        """
        return self.db
    
    def retrieve_single_order(self, parcelID):
        """
        retrieve a single order by id
        """
        order_by_id = [parc for parc in self.db if parc['id'] == parcelID][0]
        return order_by_id
    
    def cancel_order(self, ParcelID):
        """
        update parcel status to cancel
        """
        parcel_to_cancel = [parc for parc in self.db if parc['id'] == ParcelID]
        parcel_to_cancel[0]['status'] = 'cancelled'
        return parcel_to_cancel
    
    def get_orders_by_user(self, AuthorID):
        """
        retrieve all orders by a specific user given her/his username
        """
        user_orders = [parc for parc in self.db if parc['authorId'] == AuthorID][0]
        return user_orders

