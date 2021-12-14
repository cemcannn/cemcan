import requests
from bs4 import BeautifulSoup

header_param = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
ikome = requests.get("https://www.ikome.com.tr/",headers=header_param)

jobs=ikome.content
soup = BeautifulSoup(jobs,"html.parser")

all_data = soup.find_all("div",{"class":"mySlides w3-display-container w3-center"})
for data in all_data:
    print(data.img)
