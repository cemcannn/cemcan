from .arac import Arac # Arac dosyasından Arac class ını çekiyoruz fakat nokta ne işe yarıyor??
from . import arac_yonetimi # Aynı dizinde arac yonetimi dosyasını çekiyoruz.
import random # Random modülünü import ediyoruz.
import menu_yonetimi
from . import arac_veri_yonetimi

__menu_metni = """
                Seçenekler :
                [1] Araç Eklemek İçin
                [2] Araç Listelemek İçin
                [3] Araç Silmek İçin
                [4] Araç Düzenlemek İçin
                [5] Ana Menuye Donmek İçin """

def __arac_ekle(arac:Arac): # Araç ekle fonksiyonu oluşturup keyword argument olarak arac parametresini Arac classına eşliyoruz.
    if arac==None: # Eğer arac parametresi boş ise:
        arac_benzersiz_kod  = random.randint(1, 1000000) # Arac_benzersiz kod adında bir değişken  tanımlıyoruz sebebi ise aracın unique bir sayıya sahip olması, bunu da rastgele 1 ile 1000000 arasında bir rakamdan seçmesini sağlıyoruz.
        arac_serino         = input("serino giriniz: ") # Arac seri no değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        arac_marka          = input("marka giriniz: ")  # Arac marka değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        arac_model          = input("model giriniz: ")  # Arac model değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        arac_fiyat          = input("fiyat giriniz: ")  # Arac fiyat değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        arac_renk           = input("renk giriniz: ")  # Arac renk değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        arac_silindir       = input("silindir sayısını giriniz: ") 
        arac = Arac(arac_benzersiz_kod, arac_serino, arac_marka, arac_model, int(arac_fiyat), arac_renk, int(arac_silindir)) # Arac değişkenini Arac classına eşitliyoruz.

        sonuc = arac_yonetimi.arac_ekle(arac) # Sonuç değişkenine arac yonetimi dosyasında arac ekle fonksiyonunu çalıştırıp oluşturduğumuz arac değişkenini ekliyoruz.

        if sonuc[0] == False: # Eğer sonuc değişkeninin 0'ıncı indeksi False ise
            print(sonuc[1]) # Sonuç değişkeninin 1. indeksi yazdırılır
            __arac_ekle(arac) # Yukarıda eklenen arac ekle fonksiyonuna arac parametresi eklenir
        else:
            print("araç başarıyla kaydedildi") # Burayı tam anlamadım

    else:
        print("Daha önce girdiğiniz değeri kabul etmek için enter tuşuna basınız.")
        arac_serino     = input(f"serino giriniz ({arac.serino}):") # Eğer araç seri nosu araç paternine uymuyorsa bizden tekrar seri no istiyor ve araç seri no yazdırıyor.
        arac_marka      = input(f"marka giriniz ({arac.marka}): ")
        arac_model      = input(f"model giriniz ({arac.model}): ")
        arac_fiyat      = input(f"fiyat giriniz ({arac.fiyat}): ")
        arac_renk       = input(f"renk giriniz ({arac.renk}): ")
        arac_silindir   = input("silindir sayısını giriniz ({arac.silindir}): ") 

        if arac_serino == "": # Eğer bir değer vermezsek arac_seri noyu eski değer olarak bırakır.
            arac_serino = arac.serino

        if arac_marka == "":
            arac_marka = arac.marka

        if arac_model == "":
            arac_model = arac.model

        if arac_fiyat == "":
            arac_fiyat = arac.fiyat

        if arac_renk == "":
            arac_renk = arac.renk

        if arac_silindir == "":
            arac_silindir = arac.silindir

        arac = Arac(arac.benzersiz_kod, arac_serino, arac_marka, arac_model, int(arac_fiyat), arac_renk, int(arac_silindir)) # Değerleri arac değişkeninin içine kaydeder.

        sonuc = arac_yonetimi.arac_ekle(arac) # araç yönetimi modülü altında araç ekle fonksiyonuna arac değişkenini ekleyip sonuç değişkenine sabitliyoruz.

        if sonuc[0] == False: # Yine yukarıdaki sistem.
            print(sonuc[1])
            __arac_ekle(arac)
        else:
            print("araç başarıyla kaydedildi")

def menu_getir():
    while True: # Döngüyü almak için True döndürüyoruz.
        print(__menu_metni) # Menü metni yazdırıyoruz.
        secenek = int(input("arac yonetimi menu seçiminizi yapınız: ")) # Menü yöentimi seçiyoruz.
        if secenek == 1: # 1. Seçenek Araç Ekleme seçilirse:
            print("araç ekleme çalışıyor")
            __arac_ekle(None) # __arac_ekle fonksiyonuna None tanımlıyoruz.
        elif secenek == 2: # 2. Seçenek Araç Listeleme seçilirse:
            arac_listesi = arac_yonetimi.arac_listele() # Arac yönetimi modülü altında araç listele fonksiyonunu, araç listesi değişkenine eşitliyoruz.
            for arac in arac_listesi.items(): 
                print(arac)
        elif secenek == 3:
            arac_listesi = arac_yonetimi.arac_listele()
        elif secenek == 4:
            pass
        elif secenek == 5:
            menu_yonetimi.ana_menu_getir()
            pass
        else:
            print("Lütfen doğru seçeneği seçiniz!")
