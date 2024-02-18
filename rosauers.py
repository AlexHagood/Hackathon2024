from scrapper import getWebsiteHttps
import re
import json


from bs4 import BeautifulSoup

pricepattern = r'\$\d+\.\d{2}'

rosauers = getWebsiteHttps("milk")[0]
rosauers = json.loads(rosauers)
rosauers = rosauers['data']

for product in rosauers:
    print(product['attributes']['name'] + ":" + "$" + str(product['attributes']['unit_price']))
