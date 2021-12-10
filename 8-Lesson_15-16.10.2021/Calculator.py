# HesapMakinasi class ı olacak
# bu class da bir dictionary formullerın adını key olarak tutacak
# formullerin kendinisi (yani memory deki adresini) value oarak tutacak. 
# aslında fonksiyonu bir değişken olarak sozluğe
# ekliyor olacağız (hatırlayınız 13gun fonksiyonları parametre olarak taşımak)
# class daki hazır koyacağınız hesaplamalar (örneğin dort işlem) dışarıdan 
# çağrılamamalşı (hatuırlayınız private __)
 
# Bu class üzerinden fondkiyon yarıdımıyla yeni hesaplama fomksiyolarını sozluüğe ekleyebilmeliyiz.
# başka bir fonksiyonla tüm hesaplamaların listesini alabilmeliyiz
# yine başka bir fonksiyonla sozlukteki bir fonkiyonu (hesaplamayı)
# çağırıp kullanabilmeliyiz
# if bloğu kullşanılmayacak
 
from typing import Callable
 
class HesapMakinasi: # Hesap makinesi fonksiyonu oluşturuyoruz.
    def __init__(self): # 
        self.__hesaplar = dict() # Hesaplar değişkenini bir sözlüğe atıyoruz.
        self.hesaplama_ekle("topla",self.__topla) # Hali hazırda 2 adet fonksiyon eklenmiş olarak başlıyoruz.
                    # __topla foksiyonu parametre olarak diğer fonksiyona gonderildi
        self.hesaplama_ekle("çıkar",self.__cikar)
        
    def hesaplama_ekle(self, hesaplama_adi:str, hesaplama_fonksiyonu:Callable[[],int]): # Hesap makinesine hesaplama fonksiyonu eklemek için fonksiyon adını str parametresi olarak alıyoruz, onun yanında bir fonksiyon giriyoruz, bu fonksiyonu girerken değer vemiyoruz fakat bize int değer olarak dönüyor, dönen fonksiyonu da Hesap Makinesi class ının altında __hesaplar olarak tanımlanan değişkene yani dictionary e tanımlıyoruz.
                    #hesaplama_fonksiyonu parametresi altta sozluge value olarak eklendi
 
        self.__hesaplar[hesaplama_adi]=hesaplama_fonksiyonu
    
    def hesaplamalari_listele(self): # Hesap makinesi içerisindeki formülleri görmek için hesapları listele fonksiyonu yazıyoruz,hesaplar sözlüğünün içindeki değerleri for ile dönüp yazdırıyoruz.
        print("========== Liste ================")
        for h in self.__hesaplar:
            print(h)
    
    def hesaplama_cagir(self, hesaplama_adi:str) -> Callable[[],int]: # Bir hesaplama işlemini yapabilmek için hesaplama cagir fonksiyonunu kullanıyoruz, hesaplama adını str olarak istiyor fonksiyon bizden, geriye fonksiyon olarak return ediyor..
        return self.__hesaplar[hesaplama_adi]
 
    def __topla(self) -> int: 
        sayi1 = int(input("sayi1'i giriniz: "))
        sayi2 = int(input("sayi2'i giriniz: "))
        return sayi1 + sayi2
 
    def __cikar(self) -> int:
        sayi1 = int(input("sayi1'i giriniz: "))
        sayi2 = int(input("sayi2'i giriniz: "))
        return sayi1 * sayi2
    
hesap_makinasi = HesapMakinasi() # hesap makinesini bir örneklem olarak bir değişkene eşitliyoruz.
 
def abc_hesabi()->int: 
    sayi1 = int(input("sayi1'i giriniz: "))
    sayi2 = int(input("sayi2'i giriniz: "))
    sayi3 = int(input("sayi3'i giriniz: "))
 
    return sayi1 * sayi2 + sayi1 / sayi2
 
hesap_makinasi.hesaplama_ekle("abc",abc_hesabi) # abc hesabını hesap makinesi değişkeninin içinde bulunan hesaplama ekle fonksiyonunda isim ve abc fonksiyonunu girerek işliyoruz.
 
def abc2_hesabi()->int:
    sayi1 = int(input("sayi1'i giriniz: "))
    sayi2 = int(input("sayi2'i giriniz: "))
    sayi3 = int(input("sayi3'i giriniz: "))
 
    return sayi1 * sayi2 + sayi1 / sayi2
 
hesap_makinasi.hesaplama_ekle("abc2",abc2_hesabi)


 
while True:
    
    secenekler = int(input("""hesaplamaları listelemek için 1
                                \n hesap çağırmak için 2
                           """))
    
    if secenekler == 1:
        hesap_makinasi.hesaplamalari_listele()
    elif secenekler == 2:
        hesap_makinasi.hesaplamalari_listele()
        hesaplama_fonksiyonu = hesap_makinasi.hesaplama_cagir(input("hesaplama adını giriniz: "))
        sonuc = hesaplama_fonksiyonu()
        print(sonuc)
 
    else:
        print("hata yaptınız")
    
    secenek = input("çıkmak için h devam için e ye basınız")








