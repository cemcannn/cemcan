from .arac import Arac # Arac dosyasından Arac class ını çekiyoruz fakat nokta ne işe yarıyor??
from . import arac_yonetimi # Aynı dizinde arac yonetimi dosyasını çekiyoruz.
import random # Random modülünü import ediyoruz.
import menu_yonetimi
import os
import time

__menu_metni =("""
            ===========================
            Araç Yönetim Menüsü
            ===========================
            Lütfen bir seçenek seçiniz:
            (1) Araç Ekle
            (2) Araç Listele
            (3) Araç Sil
            (4) Araç Düzenle
            (5) Ana Menüye Dön
            ===========================
            """)

def __arac_ekle(arac:Arac): # Araç ekle fonksiyonu oluşturup keyword argument olarak arac parametresini Arac classına eşliyoruz.
    if arac==None: # Eğer arac parametresi boş ise:
        arac_benzersiz_kod  = random.randint(1, 1000000) # Arac_benzersiz kod adında bir değişken  tanımlıyoruz sebebi ise aracın unique bir sayıya sahip olması, bunu da rastgele 1 ile 1000000 arasında bir rakamdan seçmesini sağlıyoruz.
        arac_serino         = input("Lütfen Araç Seri Numarasını 'A000-0000' Pattern Örneğine göre Giriniz : ") # Arac seri no değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        arac_marka          = input("Lütfen Araç Markasını Giriniz : ")  # Arac marka değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        arac_model          = input("Lütfen Araç Modelini Giriniz : ")  # Arac model değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        arac_fiyat          = input("Lütfen Araç Fiyatını Giriniz : ")  # Arac fiyat değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        arac_renk           = input("Lütfen Araç Rengini Giriniz : ")  # Arac renk değişkeni tanımlayıp bunu kullanıcıdan alıyoruz.
        arac_silindir       = input("Lütfen Araç Silindir Sayısını Giriniz : ") 
        arac = Arac(arac_benzersiz_kod, arac_serino, arac_marka, arac_model, int(arac_fiyat), arac_renk, int(arac_silindir)) # Arac değişkenini Arac classına eşitliyoruz.

        sonuc = arac_yonetimi.arac_ekle(arac) # Sonuç değişkenine arac yonetimi dosyasında arac ekle fonksiyonunu çalıştırıp oluşturduğumuz arac değişkenini ekliyoruz.

        if sonuc[0] == False: # Eğer sonuc değişkeninin 0'ıncı indeksi False ise
            print(sonuc[1]) # Sonuç değişkeninin 1. indeksi yazdırılır
            __arac_ekle(arac) # Yukarıda eklenen arac ekle fonksiyonuna arac parametresi eklenir
        else:
            print("Araç Başarıyla Kaydedildi.") # Burayı tam anlamadım

    else:
        print("Daha Önce Girdiğiniz Değeri Dabul Etmek için Enter Tuşuna Basınız.")
        arac_serino     = input(f"Lütfen Araç Seri Numarasını 'A000-0000' Pattern Örneğine göre Giriniz ({arac.serino}):") # Eğer araç seri nosu araç paternine uymuyorsa bizden tekrar seri no istiyor ve araç seri no yazdırıyor.
        arac_marka      = input(f"Lütfen Araç Markasını Giriniz ({arac.marka}): ")
        arac_model      = input(f"Lütfen Araç Modelini Giriniz ({arac.model}): ")
        arac_fiyat      = input(f"Lütfen Araç Fiyatını Giriniz ({arac.fiyat}): ")
        arac_renk       = input(f"Lütfen Araç Rengini Giriniz ({arac.renk}): ")
        arac_silindir   = input("Lütfen Araç Silindir Sayısını Giriniz ({arac.silindir}): ") 

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
            print("Araç Başarıyla Kaydedildi.")

def menu_getir():
    while True: # Döngüyü almak için True döndürüyoruz.
        print(__menu_metni) # Menü metni yazdırıyoruz.
        secenek = int(input("Arac Yonetimi Menü Seçiminizi Yapınız: ")) # Menü yöentimi seçiyoruz.
        if secenek == 1: # 1. Seçenek Araç Ekleme seçilirse:
            print("Araç Ekleme Çalışıyor...")
            time.sleep(1)
            __arac_ekle(None) # __arac_ekle fonksiyonuna None tanımlıyoruz.
        elif secenek == 2: # 2. Seçenek Araç Listeleme seçilirse:
            os.system("cls")
            print("Araçlar listeleniyor...")
            time.sleep(1)
            arac_listesi = arac_yonetimi.arac_listele() # Arac yönetimi modülü altında araç listele fonksiyonunu, araç listesi değişkenine eşitliyoruz.
            for arac in arac_listesi.items(): 
                print(arac)
            print(input("Devam Etmek için Bir Tuşa Basınız..."))
        elif secenek == 3:
            os.system("cls")
            print("Araç Silme Çalışıyor...")   
            time.sleep(1)                     
            arac_listesi = arac_yonetimi.arac_listele()
            for arac in arac_listesi.items(): 
                print(arac)
            arac_yonetimi.arac_sil(int(input("Lütfen Silmek İstediğiniz Aracın Benzersiz Kodunu Giriniz : ")))
        elif secenek == 4:
            os.system("cls")
            print("Araç Düzenleme Çalışıyor...")   
            time.sleep(1)                     
            arac_listesi = arac_yonetimi.arac_listele()
            for arac in arac_listesi.items(): 
                print(arac)
            arac_yonetimi.arac_duzenle(int(input("Lütfen Düzenlemek İstediğiniz Aracın Benzersiz Kodunu Giriniz : ")))
        elif secenek == 5:
            menu_yonetimi.ana_menu_getir()
        else:
            print("Lütfen Doğru Seçeneği Seçiniz!")
