import json

class Store:
    def __init__(self, Name: str, URL: str, Address: str):
        self.name = Name
        self.url = URL
        self.Address = Address
        self.products = []


