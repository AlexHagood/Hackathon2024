#Must install beutiful soup the web scraper we are using
#Must install requests a socket library
import requests
from bs4 import BeautifulSoup
import string
""" def scrapeWebsite(websiteInput):
    

def findBrand(websiteInput):
    if(websiteInput.contains())
 """

#Returns Website Http Information Object, Takes string
#More info found here: https://www.w3schools.com/python/ref_requests_response.asp
def getWebsiteHttp(url):
    if str.isspace(url):
        return None
    print(requests.get(url))
getWebsiteHttp("https://www.walmart.com/store/1870-pullman-wa")