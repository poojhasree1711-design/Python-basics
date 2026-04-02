#webscrapping-example_1
from bs4 import BeautifulSoup
import requests

#get url
url=requests.get("https://www.carwale.com/hyundai-cars/venue/")
print(url)


#parse using html parser
soup=BeautifulSoup(url.content,"html.parser")
print(soup)

#find the data
title=soup.find("h2").text
span=soup.find("span",class_="o-j4 o-jk o-js o-jJ").text
td=soup.find("td")
#print data
print(title,span,td)

#webscrapping-example_2
import requests
from bs4 import BeautifulSoup

url = "https://www.carwale.com/hyundai-cars/venue/"
requests = requests.get(url)

soup = BeautifulSoup(requests.text, "html.parser")

tds = soup.find("tbody").find_all("tr")

for td in tds:
    name_tag = td.find("a")
    price_tag = td.find("span")

    if name_tag and price_tag:
        print(name_tag.get_text())
        print(price_tag.get_text())