from store import *

class Product:
    def __init__(self, ListingName: str, Price: float, Store: 'Store'):
        self.name = ListingName
        self.price = Price
        self.store = Store
        self.store.products.append(self)

    def addUnitData(self, Unit: str, Count: float):
        self.unit = Unit
        self.count = Count
        self.unitPrice = self.price / self.count

