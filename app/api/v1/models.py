
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

    def order(self):
        return self.db
        