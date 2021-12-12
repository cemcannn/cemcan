import requests
from bs4 import BeautifulSoup
#import lxml
#import json
from soupsieve import select_one

maksimum_sayfa_sayisi = 5
aranacak_kelime = "Türkiye"

url_root = "https://www.google.com"
url_searh_path = "/search"
url = url_root + url_searh_path

headers = {
            "charset":"utf-8",
            "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
            }

s = requests.session()
r = s.get(url, params={"q":aranacak_kelime},headers=headers)

root_css = ".tF2Cxc"
baslik_tag = "h3"
linkler_css = ".yuRUbf a"
link_text = ".TbwUpd.NJjxre"
aciklama_css = "#rso .lyLwlc"
aciklama_css2 = ".IsZvec" # aciklama_css üzerinden gittik
sayfalama_tablo_css = ".AaVjTc"



# <div class="tF2Cxc">
#         <div class="yuRUbf"> ... </div>
#         <div class="IsZvec"> ... </div>
#         ...
# </div>


sonuclar = []
def sonuclari_yukle(sonuclar):
    soup = BeautifulSoup(r.text, "html.parser")
    sonuclar_html_list = soup.select(root_css)
    for sonuc in sonuclar_html_list:
        sonuc_dict = dict()
        title = sonuc.select_one(baslik_tag).get_text()
        sonuc_url = sonuc.select_one(linkler_css)["href"]


        gecici_tag = sonuc.select_one(aciklama_css)

        #print(gecici_tag)

        if gecici_tag !=None:
            aciklama = sonuc.select_one(aciklama_css).get_text()

        sonuc_dict["title"]=title
        sonuc_dict["url"] = sonuc_url
        sonuc_dict["aciklama"]=aciklama
        sonuclar.append(sonuc_dict)

sayfalar = []
def  sayfa_linkerlini_yukle(sayfalar):
    soup = BeautifulSoup(r.text, "html.parser")
    sayfalar_html = soup.select_one(sayfalama_tablo_css).find_all("a")
    for sayfa in sayfalar_html[:-1]:
        sayfa_dict = dict()
        sayfa_url = sayfa["href"]
        sayfa_label = sayfa.attrs["aria-label"]
        sayfa_dict["title"] = sayfa_label
        sayfa_dict["url"] = sayfa_url
        sayfalar.append(sayfa_dict)

sonuclari_yukle(sonuclar)
sayfa_linkerlini_yukle(sayfalar)

i = 0
while i < maksimum_sayfa_sayisi:
    r = s.get(url_root + sayfalar[i]["url"], headers=headers)
    sonuclari_yukle(sonuclar)
    print(len(sonuclar))
    i = i + 1


print(sonuclar)

















