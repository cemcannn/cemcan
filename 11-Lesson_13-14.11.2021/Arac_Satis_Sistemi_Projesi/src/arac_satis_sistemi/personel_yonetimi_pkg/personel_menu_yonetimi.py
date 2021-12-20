# import menu_yonetimi
from .personel import Personel
from . import personel_yonetimi
import random

menu_metni = """ Seçenekler:
                [1] Personel Ekle 
                [2] Personelleri Listele  
                [3] Personel Sil 
                [4] Personel Düzenle 
                [5] Ana Menü """

def __personel_ekle(personel:Personel):
    if personel == None:
        personel_benzersiz_kod   = random.randint(1, 1000000)
        personel_tckn            = input("TCKN giriniz : ")
        personel_adi             = input("Personel adını giriniz : ")
        personel_soyadi          = input("Personel soyadını giriniz : ")
        personel_adresi          = input("Personel adresini giriniz : ")
        personel_telefonu        = input("Personel telefonunu giriniz : ")
        personel = Personel(personel_benzersiz_kod, personel_tckn, personel_adi, personel_soyadi, personel_adresi, personel_telefonu)

        sonuc = personel_yonetimi.personel_ekle(personel)

        if sonuc[0] == False:
            print(sonuc[1])
            __personel_ekle(personel)
        else:
            print("Personel başarıyla kaydedildi.") 
    
    else:
        print("Daha önce girdiğiniz değeri kabul etmek için enter tuşuna basınız.")
        personel_tckn        = input(f"TCKN giriniz ({personel.tckn}) : ")
        personel_adi         = input(f"Personel adını giriniz ({personel.adi}): ")
        personel_soyadi      = input(f"Personel soyadını giriniz ({personel.soyadi}) : ")
        personel_adresi      = input(f"Personel adresini giriniz ({personel.adres}) : ")
        personel_telefonu    = input(f"Personel telefonunu giriniz ({personel.tel}) : ")

        if personel_tckn == "":
            personel_tckn = personel.tckn
        
        if personel_adi == "":
            personel_adi = personel.adi

        if personel_soyadi == "":
            personel_soyadi = personel.soyadi
        
        if personel_adresi == "":
            personel_adresi = personel.adres
        
        if personel_telefonu == "":
            personel_telefonu = personel.tel

        personel = Personel(personel.benzersiz_kod, personel_tckn, personel_adi, personel_soyadi, personel_adresi, personel_telefonu)

        sonuc = personel_yonetimi.personel_ekle(personel)

        if sonuc[0] == False:
            print(sonuc[1])
            __personel_ekle(personel)
        else:
            print("Personel başarıyla kaydedildi.") 

def menu_getir(): 
    while True:
        print(menu_metni)
        secenek = int(input("Personel menu seçiminizi yapınız: "))
        if secenek == 1:
            print("Personel ekleme çalışıyor")
            __personel_ekle(None)
        elif secenek == 2:
            personel_listesi = personel_yonetimi.personel_listele()
            for personel_key, personel in personel_listesi.items():
                print(personel)
        elif secenek == 3:
            personel_listesi = personel_yonetimi.personel_listele()
        elif secenek == 4:
            # fatura_menu_yonetimi.menu_getir()
            pass
        elif secenek == 5:
            # menu_yonetimi.ana_menu_getir()
            pass
        else:
            print("Lütfen doğru seçeneği seçiniz!")            
            