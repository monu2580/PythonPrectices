from bs4 import BeautifulSoup
import requests

from pandas import DataFrame
import pandas as pd

from matplotlib import pyplot as plt
import matplotlib


response = requests.get("https://www.imdb.com/india/top-rated-indian-movies/?sort=us,desc&mode=simple&page=1")
soup = BeautifulSoup(response.text , 'html.parser')

"""title = []
year = []
rating = []

movieTitle = soup.find_all('td',class_="titleColumn")
for m in movieTitle:
    #print(m.find('a').text)
    title.append(m.find('a').text)
    #print(m.find('span').text)
    year.append(m.find('span').text.strip('()'))

movieRating = soup.find_all('td',class_="ratingColumn")
for n in movieRating:
    if n.find("strong") is not None:
        #print(n.find('strong').text)
        rating.append(n.find('strong').text)

print(title)
print(year)
print(rating)

dataset = list(zip(rating,year,title))

df =  pd.DataFrame(data=dataset,columns=['Movie Rating','Release Year','Movie Title'])

df.to_csv("Topmovies.csv",index=False, header=False)"""

readfd = pd.read_csv("Topmovies.csv",names=['Movie Rating','Release Year','Movie Title'])

print(readfd)

plt.plot(readfd['Movie Rating'])
plt.show()


