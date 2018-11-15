
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
        return payload

    def order_list(self):
        """
        retrieves entire list of delivery orders
        """
        return self.db
    
    def retrieve_single_order(self, parcelID):
        """
        retrieve a single order by id
        """
        single_parc = [parc for parc in self.db if parc['id'] == parcelID]
        if single_parc:
            return single_parc
        else:
            return False
        
    
    def cancel_order(self, ParcelID):
        """
        update parcel status to cancel
        """
        parcel_to_cancel = [parc for parc in self.db if parc['id'] == ParcelID]
        if parcel_to_cancel:
            parcel_to_cancel[0]['status'] = 'cancelled'
            return parcel_to_cancel
        else:
            return False
    
    def get_orders_by_user(self, AuthorID):
        """
        retrieve all orders by a specific user given her/his username
        """
        user_orders = [parc for parc in self.db if parc['authorId'] == AuthorID]
        if user_orders:
            return user_orders
        else:
            return False
