from scrapper import getWebsiteHttps
import re

from bs4 import BeautifulSoup

pricepattern = r'\$\d+\.\d{2}'

walmart = getWebsiteHttps("milk")[0]

soup = BeautifulSoup(walmart, 'html.parser')


product_title_divs = soup.find_all('span', class_='w_iUH7')

for title in product_title_divs:
    print(title.text)


