from bs4 import BeautifulSoup
import requests

#get url
url=requests.get("https://www.carwale.com/hyundai-cars/venue/")
print(url)

#parse using html parser
soup=BeautifulSoup(url.content,"html.parser")
print(soup)

#find the image
img_tag=soup.find("img",alt=lambda x: x and "Venue" in x)

#get the image
image=img_tag.get("src")

#download the image
download_image=requests.get(image)

#save the image as .jpg in a file
with open("car_image.jpg","wb") as file:
    file.write(download_image.content)