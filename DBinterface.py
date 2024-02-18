import redis
from product import *

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
#r = redis.Redis(host='redis-10741.c267.us-east-1-4.ec2.cloud.redislabs.com', port=10741, decode_responses=True)


def store_product(inputProduct: Product, key):
    r.set(key, inputProduct.jsonify())
    print(f"Stored product {inputProduct.name} under key {key}")


def drop_product(key):
    pass


def retrieve_product(key):
    returnProduct = r.get(key)
    returnProduct = json.loads(returnProduct)
    print(f"Fetched product {returnProduct['name']} at price {returnProduct['price']}")

