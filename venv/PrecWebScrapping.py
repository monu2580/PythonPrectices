import requests as req
from bs4 import BeautifulSoup
#from beautifulscraper import BeautifulSoup as bs
#wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
wiki1 = "https://www.website_to_crawl.com"

response = req.get(wiki1,timeout=5)

page_content=BeautifulSoup(response.content,"Html.parser")

price=page_content.find_all(class_="main_price")

print(response)

