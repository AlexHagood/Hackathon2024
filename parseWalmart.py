from scrapper import getWebsiteHttps
import re

from bs4 import BeautifulSoup

def walmartScraping(inputData):
    pricepattern = r'\$\d+\.\d{2}'

    soup = BeautifulSoup(inputData, 'html.parser')


    product_title_divs = soup.find_all('span', class_='w_iUH7')

    count = 0
    outputlist = []

    for title in product_title_divs:
        if(title.text.count('reviews')==0):
            if(count == 0):
                holderstring = title.text
                count = count + 1
            elif(title.text.count('$')>0):
                holdernumber = title.text.find('$')
                outputlist.append((holderstring,title.text[holdernumber:]))
                holderstring = ""
                count = 0
    return outputlist
