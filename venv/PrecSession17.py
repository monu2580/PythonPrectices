"""import requests

# response = requests.get('https://twitter.com/narendramodi')
# print(response.text)

# url = ('http://delhihighcourt.nic.in/dhc_case_status_list_new.asp')
# data = {"sno":2,"party":"Rahul","pyear":2018}
# response = requests.post(url=url,data=data)
# print(response.text)


response = requests.get('https://twitter.com/dna')
print(response.text)"""
import requests
from bs4 import BeautifulSoup

#response = requests.get('https://twitter.com/dna')
#response = requests.get('https://twitter.com/narendramodi')
#response = requests.get('http://zeenews.india.com/')
response = requests.get('https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=600ca544-31f5-4bd8-ae38-ea4014c93bab&pf_rd_r=0BGMANQ4YJQW1Y0V5GB9&pf_rd_s=right-4&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_india_tr_rhs_1')
soup = BeautifulSoup(response.text,"html.parser")

# print(soup)  #return All Html Content
# print(type(soup)) # type - BeautifulSoup
# print(soup.prettify()) ## it will retur all Htm code with Arrangment
#
# print(soup.title.text)
#
# children = soup.children
# for child in children:
#     print(child)
#
#
# pTags = soup.find_all('p')   #priint All <p> tag
# for tafg in pTags:
#     print(tafg)
#
# divTags = soup.find_all('div')   #priint All <div> tag
# for tafg in divTags:
#     print(tafg)
#
# divTags = soup.find_all('div')
# print(divTags[0]) #return First <div> Tag
# print(divTags[0].text) # only text Data \
#
# divTagsOnZeroIndex = soup.find('div')
# print(divTagsOnZeroIndex.text)  #return All Text Data Of 0 index

# divTags = soup.find_all('div', class_='js-tweet-text-container')   #priint All <div> tag  #print All Tweets of Narender Momdi
# for tafg in divTags:
#     print(tafg.text)

# newsData = soup.find_all('h3')
# for newsD in newsData:
# #     print(newsD.text)
# newsData = soup.find_all('div',class_='mini-con')
# print(divTags[0]) #return First <div> Tag #First News Heading
# for newsD in newsData:
#     print(newsD.text)

# movies = []
# imdbMovieData = soup.find_all('td',class_='titleColumn')
# for imdbTopMovie in imdbMovieData:
#     #print(imdbTopMovie.text) #Show All Top 10 Movie List
#     movies.append(imdbTopMovie.text.strip()) # Store All Data in List
#
# print(movies)

imdbRatingData = soup.find_all('td',class_='ratingColumn')
#print(imdbRatingData[0].find('strong').text)

imdbRatingData = soup.find_all('td',class_='ratingColumn')
for imdbRate in imdbRatingData:
    if imdbRate.find('strong') is not None:
        print(imdbRate.find('strong').text)
