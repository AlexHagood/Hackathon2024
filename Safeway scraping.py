from scrapper import getWebsiteHttps
import re

from bs4 import BeautifulSoup

pricepattern = r'\$\d+\.\d{2}'

safeway = getWebsiteHttps("milk")[0]

soup = BeautifulSoup(safeway, 'html.parser')


product_price_divs = soup.find_all('div', class_='product-price')
product_title_divs = soup.find_all('div', class_='product-title__text')

for product, price in zip(product_title_divs, product_price_divs):
    print(price.text[11:16] + ":" + product.text)

