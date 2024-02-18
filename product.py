from store import *


class Product:
    def __init__(self, ListingName: str, Price: float, Store: 'Store'):
        self.name = ListingName
        self.price = Price
        self.store = Store
        self.store.products.append(self)

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'store': self.store.name
        }
    
    def jsonify(self):
        return json.dumps(self.to_dict())


