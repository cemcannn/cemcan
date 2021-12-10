# bütün e-mail adreslerini bulunuz
# bütün rakamsal ifadeleri bulunuz
# nokta ile biten bütün kelimeleri bulunuz (örn. abc.)
# Türkiye kelimesinin geçtiği cümleyi tüm olarak getiriniz
# başı "Azerb" sonra gelen karakterin e veya olmayan sonu "ycan"  ile biten kelimeleri bulunuz.
# başı "Azerb" sonra gelen karakterin e veya olmayan sonu "ycan"  ile biten kelimeleri "Azerbaycan" olarak değiştiriniz (tip sub  fonksiyonu)
import re

metin = "Türkiye veya resmî adıyla Türkiye Cumhuriyeti, 2021 topraklarının büyük bölümü Anadolu'da, küçük bir bölümü ise Balkan Yarımadası'nın güneydoğu uzantısı olan Trakya'da yer alan ülke. Kuzeybatıda Bulgaristan, batıda Yunanistan, kuzeydoğuda Gürcistan, doğuda Ermenistan,info@turkiye.gov İran ve Azerbaycan'ın Azerbeycan Azerbycan ekslav toprağı Nahçıvan, güneydoğuda ise Irak ve Suriye komşusudur. Güneyini Kıbrıs adası ve Akdeniz, Batısını Ege Denizi ve kuzeyini Karadeniz çevreler. cem@abb Marmara Denizi ise İstanbul Boğazı ve Çanakkale Boğazı ile birlikte Anadolu'yu Trakya'dan yani Asya'yı Avrupa'dan ayırır. Türkiye, Avrupa ve Asya'nın kavşak noktasında yer alması sayesinde önemli bir jeostratejik güce sahiptir. info@turkiye.gov.tr"

aranan_kelime = "\w+@\w+\.[a-z]+\.?"
result = re.findall(aranan_kelime, metin)
print(result)

aranan_kelime2 = "\d+"
result = re.findall(aranan_kelime2, metin)
print(result)

aranan_kelime3 = "\w+\."
result = re.findall(aranan_kelime3, metin)
print(result)

aranan_kelime4 = ".+?[Tt]ürkiye.+?\."
result = re.findall(aranan_kelime4, metin)
print(result)

aranan_kelime5 = "Azerb[ae]?ycan"
result = re.findall(aranan_kelime5, metin)
print(result)

yerine_gelecek_kelime = "Azerbaycan"

result = re.sub(aranan_kelime5,yerine_gelecek_kelime,metin)
print(result)