
parcels = []

class Parcels:
    """
    Class with CRUD functionalities on the Parcels resource
    """
    def __init__(self):
        self.db = parcels

    def create_order(self, item, pickup, dest, pricing):
        """
        instance method to generate new entry into delivery orders list
        """
        payload = {
            "id" : len(self.db) + 1,
            "itemName" : item,
            "pickupLocation" : pickup,
            "destination" : dest,
            "pricing" : pricing
        }
        self.db.append(payload)

    def order_list(self):
        """
        retrieves entire list of delivery orders
        """
        return self.db
    
    def retrieve_single_order(self, parcelID):
        """
        retrive a single order by id
        """
        order_by_id = [parc for parc in self.db if parc['id'] == parcelID][0]
        return order_by_id

        