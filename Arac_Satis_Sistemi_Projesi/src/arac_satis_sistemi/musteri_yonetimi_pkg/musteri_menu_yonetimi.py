# import menu_yonetimi
from .musteri import Musteri
from . import musteri_yonetimi

menu_metni = """ Seçenekler:
                [1] Müşteri Ekle 
                [2] Müşterileri Listele  
                [3] Müşteri Sil 
                [4] Müşteri Düzenle 
                [5] Ana Menü """

def __musteri_ekle(musteri:Musteri):
    if musteri == None:
        musteri_tckn        = input("TCKN giriniz : ")
        musteri_adi         = input("Müşteri adını giriniz : ")
        musteri_soyadi      = input("Müşteri soyadını giriniz : ")
        musteri_adresi      = input("Müşteri adresini giriniz : ")
        musteri_telefonu    = input("Müşteri telefonunu giriniz : ")
        musteri = Musteri(musteri_tckn,musteri_adi,musteri_soyadi,musteri_adresi,musteri_telefonu)

        sonuc = musteri_yonetimi.musteri_ekle(musteri)

        if sonuc[0] == False:
            print(sonuc[1])
            __musteri_ekle(musteri)
        else:
            print("Müşteri başarıyla kaydedildi.") 
    
    else:
        print("Daha önce girdiğiniz değeri kabul etmek için enter tuşuna basınız.")
        musteri_tckn        = input(f"TCKN giriniz ({musteri.tckn}) : ")
        musteri_adi         = input(f"Müşteri adını giriniz ({musteri.adi}): ")
        musteri_soyadi      = input(f"Müşteri soyadını giriniz ({musteri.soyadi}) : ")
        musteri_adresi      = input(f"Müşteri adresini giriniz ({musteri.adres}) : ")
        musteri_telefonu    = input(f"Müşteri telefonunu giriniz ({musteri.tel}) : ")

        if musteri_tckn == "":
            musteri_tckn = musteri_tckn
        
        if musteri_adi == "":
            musteri_adi = musteri_adi

        if musteri_soyadi == "":
            musteri_soyadi = musteri_soyadi
        
        if musteri_adresi == "":
            musteri_adresi = musteri_adresi
        
        if musteri_telefonu == "":
            musteri_telefonu = musteri_telefonu

        musteri = Musteri(musteri.tckn, musteri_adi, musteri_soyadi, musteri_adresi, musteri_telefonu)

        sonuc = musteri_yonetimi.musteri_ekle(musteri)

        if sonuc[0] == False:
            print(sonuc[1])
            __musteri_ekle(musteri)
        else:
            print("Müşteri başarıyla kaydedildi.") 

def menu_getir(): 
    while True:
        print(menu_metni)
        secenek = int(input("Müşteri menu seçiminizi yapınız: "))
        if secenek == 1:
            print("Müşteri ekleme çalışıyor")
            __musteri_ekle(None)
        elif secenek == 2:
            musteri_listesi = musteri_yonetimi.musteri_listele()
            for musteri_key, musteri in musteri_listesi.items():
                print(musteri)
        elif secenek == 3:
            musteri_listesi = musteri_yonetimi.musteri_listele()
        elif secenek == 4:
            # fatura_menu_yonetimi.menu_getir()
            pass
        elif secenek == 5:
            # menu_yonetimi.ana_menu_getir()
            pass
        else:
            print("Lütfen doğru seçeneği seçiniz!")            
            