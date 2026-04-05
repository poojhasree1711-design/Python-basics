import requests
from bs4 import BeautifulSoup

base="https://www.zaubacorp.com"

url="https://www.zaubacorp.com/companysearchresults/CHENNAI"
requests=requests.get(url)
soup=BeautifulSoup(url.content, "html.parser")

rows=soup.find_all("tr")