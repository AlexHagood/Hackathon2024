from scrapper import getWebsiteHttps
import re
import json


from bs4 import BeautifulSoup
def rosauersParser(inputData):
    pricepattern = r'\$\d+\.\d{2}'
    
    rosauers = json.loads(inputData)
    rosauers = rosauers['data']

    outputList = []

    for product in rosauers:
        outputList.append((product['attributes']['name'],"$"+str(product['attributes']['unit_price'])))
    return outputList
