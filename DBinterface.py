import redis
from redis.commands.json import path
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

import random


from product import *

# r = redis.Redis(host='localhost', port=6379, decode_responses=True)

print("connecting to db...")
r = redis.Redis(
  host='redis-10741.c267.us-east-1-4.ec2.cloud.redislabs.com',
  port=10741,
  password='QkT94imyPmsRtV6R2N7RHH8yw7wJWAvE',
  db=0,
  decode_responses=True)
print("connected...")


print("index creation")
index = r.ft("idx:prod")
print("index create_index")
index.create_index(TextField("$.name", as_name="name"), definition=IndexDefinition(prefix=["prod:"],index_type=IndexType.JSON),)
print ("completed creation of index")

def uploadProducts(productList : list[Product]):
    for product in productList:
        randomID = random.randint(1,100)
        r.json.set(f"prod:{randomID}", Path.root_path(), product.jsonify())




def searchDB(query: str):
    res = index.search(Query(query))
    print("Documents found:", res.total)



def create_store(inputProduct: Product, key):
    r.set(key, inputProduct.jsonify())
    print(f"Stored product {inputProduct.name} under ID {key}")


def drop_product(key):
    dropped = r.delete(key)
    if dropped:
        print(f"product ID {key} removed")
    else:
        print(f"product ID {key} not found")
        


def retrieve_product(key):
    returnProduct = r.get(key)
    returnProduct = json.loads(returnProduct)
    print(f"Fetched product {returnProduct['name']} at price {returnProduct['price']}")



