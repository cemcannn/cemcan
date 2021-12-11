###  installation / python dışında yüklemes iyapılmalı.
# pip install beautifulsoup4
# pip install lxml
# pip install html5lib

html_doc = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,"html.parser")

#print(soup.prettify())

print(soup.title)

print(soup.title.name)

print(soup.title.string)

print(soup.title.parent)

print(soup.title.parent.name)
print(soup.title.parent.string) # çünkü head içinde string ifa de yoktur

print(soup.p)

print(soup.p["class"])

print(soup.a)

print("--------------------- bütün a tagları")
butun_a_taglari = soup.find_all("a")
print(butun_a_taglari)

import requests


for a in butun_a_taglari:
    print(type(a))
    print(a["href"])
    r = requests.get(a["href"])
    #print(r.text)

    soup2 = BeautifulSoup(r.text,"html.parser")
    print(soup2.find_all("p"))

print("---------------------")
print(soup.get_text())


### beautifulsoup objects

### tag

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')

tag = soup.b
print(type(tag))



