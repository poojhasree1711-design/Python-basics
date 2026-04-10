# def words(string_1):
#     words=string_1.split()
#     result=[]
#     for word in words:
#         if word not in result:
#             result.append(word)
#     return result
    
# words("I'm a boy living in cuddalore which is in tamil nadu")

string_2="I'm a boy living in cuddalore which is in tamil nadu"
# print(string_2.split("in"))
# print("".join(string_2))
# print(dir(str))

result=[]
word=""
for i in range(len(string_2)):
    word+=string_2[i]
    if word.endswith("in"):
        result.append(word.strip())
        word=""
    if word:
        result.append(word.strip())
    print(result)

print(string_2.rpartition("in"))

from bs4 import BeautifulSoup
import requests

url="https://www.carwale.com/hyundai-cars/venue"
request=requests.get(url)

soup=BeautifulSoup(request.text,"html.parser")
print(soup)

title=soup.find("h2").text
span=soup.find("span",class_="o-j4 o-jk o-js o-jJ").text
print("model name:",title,"price:",span)


