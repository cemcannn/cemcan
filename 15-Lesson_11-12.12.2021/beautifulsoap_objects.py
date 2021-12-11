### beautifulsoup objects
### tag
from bs4 import BeautifulSoup
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')

tag = soup.b
print(type(tag))
print(tag.name)


### attrribute
tag = BeautifulSoup('<b id="boldest" class="font_class color_class">bold</b>', 'html.parser').b
print(tag['id'])
print(tag.attrs)

####### comment

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
metin = soup.b.string
print(metin)


######## html (xml) tree (ağacı) içinde dolaşmak - navigation

html_doc = """
<html><head><title>The Dormouse's story</title></head>
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

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.head)

print(soup.body.p.b) # ilk p altındaki b tagına gitmiş olduk

print(soup.find_all("a"))

######################33 content ve child
print("----------------------------- content ve child")
body_content = soup.body.contents
print(body_content)
print("------------------")
print(body_content[1])

print("----------------------")
print(soup.body.children)
for child in soup.body.children:
    print(child)

print("----------------------")
print(soup.body.find_all("p")[1].contents)

##### sideway - yanlara dopru gitmek


from bs4 import BeautifulSoup

sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", 'html.parser')
print(sibling_soup.prettify())

#<a>
# <b>
#  text1
# </b>
# <c>
#  text2
# </c>
#</a>

print(sibling_soup.b.next_sibling)
# <c>text2</c>

print(sibling_soup.c.previous_sibling)
# <b>text1</b>

print(sibling_soup.b.next_sibling.string)
# text2

###################### yukarı aşağı hareket

from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<div id="first_div">
   <div>
        merhaba
          <div>
              test
                 <div>
                 </div>
          </div>
   </div>
</div>

<p class="story">...</p> """


soup = BeautifulSoup(html_doc, 'html.parser')


last_a_tag = soup.find("a", id="link3")
print(last_a_tag)
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

print(last_a_tag.next_sibling)
# ';\nand they lived at the bottom of a well.'

print(last_a_tag.next_element)
#Tillie

# beauutifusoap boşluk e metinleri de element olarak kabul eder
print(last_a_tag.next_element.next_element.next_element.next_element)

###################################################### searching

html_doc = """
<html><head><title>The Dormouse's story</title></head>
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
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.find_all(["a", "b"]))

# sayfada kullanılan bütün tag ları aramak

for tag in soup.find_all(True):
    print(tag.name)


##### id üzerinden search etmek
print(soup.find_all(id="link2"))


##################################3 output
import requests
r = requests.get("https://www.haberler.com/")

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

#print(soup.body.prettify())
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#line-numbers
print("------------------------------------------------------------")
for tag in soup.find_all('p'):
    print(repr((tag.sourceline, tag.sourcepos, tag.string)))








