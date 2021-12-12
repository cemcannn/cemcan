import requests
import json
import lxml
from bs4 import BeautifulSoup

url = "https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+page+site+area/bugun"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

doviz_kurlari_tablo = soup.select(".kurlarTablo")

print(doviz_kurlari_tablo) # ekrana hiç bir liste gelmediğini
# gordukten sonra sayfada yaptığımız araştırma sonucunda verilerin xml oalrak geldiğini keşfettik
# ozaman kurgumuzu xml den veri çekecek şekild eğiştiriyoruz

url2= "https://www.tcmb.gov.tr/kurlar/today.xml?_=1635942061705"
r2 = requests.get(url2)
soup2 = BeautifulSoup(r2.text, 'lxml')

print(soup2.prettify())

doviz_kurlari_xml_list = soup2.find_all("currency")

doviz_kurlari = []

for doviz_kuru_xml in doviz_kurlari_xml_list:
    doviz_kuru_dict=dict()
    for currency_detail in doviz_kuru_xml:
        #print(currency_detail.name)
        if currency_detail.name != None:
            doviz_kuru_dict[currency_detail.name] = currency_detail.text
    doviz_kurlari.append(doviz_kuru_dict)


print(doviz_kurlari[10])


tarih = soup2.find("tarih_date")["tarih"]
print(tarih)






