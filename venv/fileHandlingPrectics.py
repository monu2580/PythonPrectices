filw1 = {101:"Deepesh", 103:"Jivesh"}
jsonData =    {
      "bookstore": [
        {
          "price": "100 INR", 
          "name": "Objective C", 
          "author": "Steve Jobs"
        }, 
        {
          "price": "200 INR", 
          "name": "Android Programming", 
          "author": "Aaron Brooks"
        }, 
        {
          "price": "300 INR", 
          "name": "Advance Java", 
          "author": "David Smith"
        }
    ]
}

#json1 = {"mncx":"djjfkk","jkjjhfn":"jfdjhbjf","vbfhf":"jfjbkjd","vknvjknv":"jbjknjcn"}
#for i,j in json1.items():
#    print("{0:10}  *****  {1:10}".format(i,j))

# import json
# import urllib.request
# from pprint import pprint
#
# websource = urllib.request.urlopen('http://www.masslottery.com/data/json/games/lottery/recent.json')
# data = json.loads(websource.read().decode())
# pprint(data)




# import pprint
# import json
# from urllib.request import urlopen # (Only used to get this example)
#
# # Getting a JSON example for this example
# r = urlopen("https://mdn.github.io/fetch-examples/fetch-json/products.json")
# text = r.read()

# To print it
#pprint.pprint(json.loads(text))


from bs4 import BeautifulSoup
import urllib.request

webpage = "http://www.masslottery.com/games/lottery/large-winningnumbers.html"

websource = urllib.request.urlopen(webpage)
soup = BeautifulSoup(websource.read(), "html.parser")
span = soup.find("span", {"id": "winning_num_0"})
print (span)
