from bs4 import BeautifulSoup
import requests

r=requests.Session()
url = "https://www.facebook.com/login"


loginData = {"email":"monu9226","pass":"1234567890"}
res= r.get(url)
r.post(url,data=loginData)

page_content=BeautifulSoup(res.content,"html.parser")
print(page_content.prettify())
# for i in res:
#     for j in i:
#         print(j)