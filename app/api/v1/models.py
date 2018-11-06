
parcels = []

class Parcels:

    def __init__(self):
        self.db = parcels

    def create_order(self, item, pickup, dest, pricing):
        payload = {
            "id" : len(self.db) + 1,
            "itemName" : item,
            "pickupLocation" : pickup,
            "destination" : dest,
            "pricing" : pricing
        }
        self.db.append(payload)

    def order_list(self):
        return self.db
    
    def retrieve_single_order(self, parcelID):
        order_by_id = [parc for parc in self.db if parc['id'] == parcelID][0]
        return order_by_id

        