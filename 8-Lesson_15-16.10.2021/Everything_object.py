# i = int(2)
 
# s = str("merhaba")
 
# class MyClass:
#     pass
 
# c = MyClass()
 
# def my_func():
#     pass
 
# abc = my_func
 
# # eğer bütün objeler eşit ise aşağıdaki kuralları sağlamalı
# # 1. başka bir fonksiyona veya class a  parametre olarak verilebilmeli
# # 2. bir fonksiyondan dondürülebilmeli
# # 3. bi rdeğişkene atanabilmeli
 

class Insan(): #Insan class ı oluşuturuldu.
    def __init__(self): 
        self.isim="murat" # isim Murat olarak tanımlandı 
    def yuru(self, adim_sayisi:int) -> int: # Yuru fonksiyonu tanımlandı int bir değer alacak dışarıya int değer verecek.
        print(str(adim_sayisi) + " adım yüründü") # Çıkan int değeri str ifadeye çevirip ekrana yazdırır.
        return adim_sayisi 
 
# bir class ı bir fonksiyona parametre olarak geçtik
def insani_yurut(insan:Insan): #Fonksiyon içinde insan diye bir değişken tanımladık bu değişkeni Insan class ına eşitledik.
    insan.yuru(34) #Bu fonksiyon içinde Insan class ına eşitlenen insan değişkenininiçinde yuru fonksiyonunu çağırdık ve yuru fonksiyonunun içinde bizden adım sayısı soruyor, bunu da 34 adım olarak girdik
 
insani_yurut(Insan()) # Artık insanı yürüt fonksiyonunu çağırdığımızda bizden bir class isteyecek, class olmadığı için Insan class ını girdik ve çıkan kaç adım yürüğünü ekrana print etti.

# bir fonksiyonu ı bir fonksiyona parametre olarak geçtik
 
from typing import Callable # Callable modülünü çağırır.
 
def adim_sayisi_getir(): # adim sayısı getir fonksşyonu oluşturuyoruz.
    return 3 #Bu fonksiyon 3 sayısını return ediyor.
 
def insani_yurut_fonksyion(yuru_fonksiyonu:Callable[[],int]): #insanı yurut fonksiyonu oluşturuyoruz. Bu fonksiyona yuru fonksiyonu parametresi giriliyor, bu da bir fonksiyonu çağırıyor, fonksiyon çağırılırken değer vermiyoruz,çağırılan fonksiyon da int değer ile geliyor.
    adim_sayisi = yuru_fonksiyonu() # Adım sayısı değişkeni yuru fonksiyonu parametresine eşitleniyor.
    print(Insan().yuru(adim_sayisi)) # Insan class ının yuru fonksiyonu adım sayısı değişkeni ile çağırılıyor.
 
insani_yurut_fonksyion(adim_sayisi_getir) #insanı yürüt fonksiyonu adım sayısı getir fonksiyonu ile çağırılıyor, adım sayısı getir fonksiyonu da 3 sayısını return ediyordu.
 
# kural 2 testleri :  bir fonksiyondan parametre olarak dondürülebilir

# object return oluyor
def insan_dondur(): # İnsan döndür fonksiyonu oluşturup Insan class ını return ediyoruz.
    return Insan() 
 
# fonksiyon return oluyor
def yuru_fonksiyonu_dondur(): # Insan class ının yürü fonksiyonunu return ediyoruz.
    return Insan().yuru # fonksiyon değer olarak doner, fonksiyonu çağırmıyoruz, eğer () açık kapatsaydık fonksiyonu çağırırdık.
    # return Insan().yuru() # bu üstteki satır ile aynı şey değil. burası int doner
 
print(type(yuru_fonksiyonu_dondur())) # Bunun bir class metod olduğunu görüyoruz.
 
a_fonksiyon = yuru_fonksiyonu_dondur() # yuru fonksiyon dondur değerini bir değişkene atıyoruz.
a_fonksiyon(3) #bu değişkeni çağırdığımızda bizden adım sayısı istiyor ve adım sayısı olarak 3 girdiğimizde bize kaç adım atıldığını veriyor.
 
yuru_fonksiyonu_dondur()(5) # bu fonksiyon direkt çağırdığımızda önce Insan.yuru fonksiyonunu çağıracak ikinci parantez aç kapada ise kaç adım atılması gerktiği yazılacaktır.
 
# diğer bir ornek fonksiyon değer geriye dondurulebilir.
# topla2 fonksiyonu topla fonksiyonunu geriye donduruyor
 
def topla(a:int,b:int): # Topla fonksiyonu oluşturuluyor ve bu fonksiyon a ve b adında 2 int parametresi alıyor.
    print(str(a+b)) # print yazıyor olmanız geriye değer dondüğü anlmaına gelmez
    toplam = a+b #a ile b değerinin toplamının ekrana yazılmasından ayrı olarak bir değişken tanımlanıp burada a ve b değerleri toplanır, bu değişkende return edilebilir ve topla 2 fonksiyonunda topla fonksiyonu çalıştırılıp print edilirse bu değerler ekrana yazdırılabilir.
    return toplam
 
def topla2():
    return topla
 
g = topla2()(3,5)
print(g)
 
# kural 3 : değikene atanabilirler
 
insan = Insan() #insan class ını insan değişkenine atıyoruz
 
def carp(a:int, b:int) -> int: #carp fonksiyonu 2 int değer olan a ve b değeri alıp dışarıya int değer veriyor.
    return a * b
 
benim_carpma_fonksiyonum = carp #carp fonksiyonunu bir değişkene atıyoruz.
 
benim_carpma_fonksiyonum(3,6) #değişkene 3 ve 6 değerini verdiğimizde bize bunların çarpımını döndürür fakat yazmaz

# kural 1 ikinci bolüm: yani bir class ın veya bir fonksiyonun 
# bir class a parametre olarak geçilmesi

import datetime
an = datetime.datetime.now()

class Insan:
    isim=""
 
class Ogrenci(): 
    def __init__(self, insan:Insan, dogum_yili:int,baz_yil:int, 
                yas_hesaplama_fonksiyonu:Callable[[int,int],int]) :
        self.isim=insan.isim
        self.dogum_yili = dogum_yili
        self.baz_yil=baz_yil
        self.yh_fonksiyonu = yas_hesaplama_fonksiyonu
 
    def ekrana_yaz(self):
        yas = self.yh_fonksiyonu(self.dogum_yili,self.baz_yil)
        print(self.isim, self.dogum_yili, yas)


 
cem=Insan()
cem.isim = "Cem"
 
def miladi_yas_hesapla(dogum_yili:int, baz_alinacak_yil:int) -> int:
    return baz_alinacak_yil - dogum_yili
 
# Turkiye versiyonu : Miladi takvim
ogrenci = Ogrenci(insan=cem,dogum_yili=1988,baz_yil=an.year,yas_hesaplama_fonksiyonu=miladi_yas_hesapla)
 
ogrenci.ekrana_yaz()
 
class Insan:
    def __init__(self, isim:str, ulke:str):
        self.isim = isim
        self.ulke = ulke
 
    def yas_hesaplama_fonksiyonu_dondur(self) -> Callable[[int,int],int]:
        if self.ulke == "Turkiye":
            return self.miladi_yas_hesapla
 
        elif self.ulke == "Kore":
            return self.kore_yas_hesapla
        else:
            return self.rumi_yas_hesapla
    
    def miladi_yas_hesapla(self, dogum_yili:int, baz_alinacak_yil:int) -> int:
        return baz_alinacak_yil - dogum_yili
 
    def kore_yas_hesapla(self, dogum_yili:int, baz_alinacak_yil:int) -> int:
        return baz_alinacak_yil - dogum_yili -1
    
    def rumi_yas_hesapla(self, dogum_yili:int, baz_alinacak_yil:int) -> int:
        return baz_alinacak_yil - dogum_yili -2

cem = Insan("cem","Kore")

hesaplama_fonksiyonu = cem.yas_hesaplama_fonksiyonu_dondur()

sonuc = hesaplama_fonksiyonu(1980, 2021)

print(sonuc)

