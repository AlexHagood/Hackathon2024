from scrapper import getWebsiteHttps
import re

from bs4 import BeautifulSoup

def safewayParser(keyWord):
    pricepattern = r'\$\d+\.\d{2}'
    
    safeway = getWebsiteHttps(keyWord)[2]
    
    soup = BeautifulSoup(safeway, 'html.parser')
    
    
    product_price_divs = soup.find_all('div', class_='product-price')
    product_title_divs = soup.find_all('div', class_='product-title__text')

    outputList = []
    
    for product, price in zip(product_title_divs, product_price_divs):
        outputList.append((product.text, price.text[11:16]))
    print(str(outputList))
parseSafeway("Milk")