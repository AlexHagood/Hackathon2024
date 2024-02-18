
class Product:
    def __init__(self, ListingName: str, Price: float, Store: str):
        self.name = ListingName
        self.price = Price
        self.store = Store

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'store': self.store
        }
    
    def jsonify(self):
        return json.dumps(self.to_dict())
    


