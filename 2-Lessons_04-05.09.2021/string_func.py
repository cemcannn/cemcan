import os

#Açıklama için kulllanılır.
#Replace : metni yazarken hata yapılırsa replace fonksiyonu ile yapılan hatalı kelimeler değiştirilebilir.
metin = "merhgbg nasılsın" 
sonuc = metin.replace("g","a") # 1. parametre değiştirilecek ifade, 2. ifade yerine koyulacak ifade.
print(sonuc)

os.system ("cls")

#UPPER : Metni büyük harfe çevirir.
il = "izmir"

buyuk_harfli_il = il.upper()
print(buyuk_harfli_il)

#LOWER : Meetni küçük harfe çevirir.

kucuk_harfli_il = buyuk_harfli_il.lower()
print(kucuk_harfli_il)

os.system ("cls")

#SPLİT : listeleri hangi karakter ile bölmek istediğini soruyor.

meyveler = "elma,armut,karpuz"
print(meyveler)
meyveler_listesi = meyveler.split(",")
print(meyveler_listesi)

print(type(meyveler_listesi))

#help(list) # liste hakkında bilgi verir

os.system ("cls")

#SPLİTLİNES : yeni satırlara göre ayrıştırır.

buyuk_metin = "merhaba nasılsın? \n iyiyim"
splitlines_metin = buyuk_metin.splitlines()
print(splitlines_metin)

os.system ("cls")

#STRIP = metnin her iki tarafındaki boşlukları siler.
#CAPITALIZE = metnin ilk harfini büyük yapar.
metin1= "     Merhaba Nasılsın     "
print(metin1)

print(metin1.strip().lower().capitalize())

os.system ("cls")

buyuk_harf_testi="merhaba"

print(buyuk_harf_testi.isupper())
print(buyuk_harf_testi.isnumeric())

print(buyuk_harf_testi.index("h")) #"h" harfi kaçıncı sıradaysa onu gösteriyor.
print(buyuk_harf_testi.find("h")) #"h" harfi kaçıncı sıradaysa onu gösteriyor.
print(buyuk_harf_testi.find("2")) # find aynı zamanda 2'yi arattığında bir şey bulamazsa -1 verir fakat index hata verir.

print(buyuk_harf_testi.count("a")) # "a" harfi kaç defa geçiyor ona bakılır.

os.system ("cls")

metin3="holaamigo"
print(len(metin3)) # metnin uzunluğunu verir.

#WORKSHOP
# request = talep
#requirement = gereksinim


#1. kullanıcıdan metin alınacak.
#2. metin içindeki bütün kelimeler büyük harf yapılacak ve ekrana yazdırılacak.
#3. metin içindeki bütün kelimeler büyük harf yapılacak ve ekrana yazdırılacak.
#4. metin içindeki a harflerinin sayısı ekrana yazdırılacak (tip: eğer yoksa program hata vermemeli)
#5. metnin tamamının harflerinin sayısı ekrana yazdırılacak
#6. metnin içindeki kelime sayısı ekrana yazdırılacak ( tip: strip)

# Acceptance Criteria = Kabul kriterleri

#1. Metni güzel bir kelime ile girmesini talep et.
#2. metin içinde en az 1 "a" harfi geçmeli

os.system ("cls")

talep = input("Lütfen içinde en az 3 'a' harfi geçecek bir kelime yazınız = ")
print(talep.title())
buyuk_harf_talep = talep.upper()
print("==========================")
print(buyuk_harf_talep)
print("==========================")
print(buyuk_harf_talep.count("A"))
print("==========================")
print(len(buyuk_harf_talep))
print("==========================")
sonuc = buyuk_harf_talep.strip().split(" ")
print(len(sonuc))
