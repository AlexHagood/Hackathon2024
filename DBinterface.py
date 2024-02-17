import redis


r = redis.Redis(host='localhost', port=6379, decode_responses=True)
#r = redis.Redis(host='redis-10741.c267.us-east-1-4.ec2.cloud.redislabs.com', port=10741, decode_responses=True)

def get_price():
    pass
