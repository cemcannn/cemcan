# import menu_yonetimi
from arac_yonetimi_pkg import arac_veri_yonetimi
from musteri_yonetimi_pkg import musteri_veri_yonetimi
from personel_yonetimi_pkg import personel_veri_yonetimi
from .fatura import Fatura
from . import fatura_yonetimi
import random
from datetime import datetime

menu_metni = """ Seçenekler:
                [1] Fatura Ekle 
                [2] Faturaları Listele  
                [3] Fatura Sil 
                [4] Fatura Düzenle 
                [5] Ana Menü """

def __fatura_ekle(fatura:Fatura):
    if fatura == None:
        fatura_benzersiz_kod    = random.randint(1, 1000000)
        fatura_no               = input("Fatura no giriniz : ")
        arac_veri_yonetimi.arac_listele()
        arac                    = input("Araç benzersiz kod giriniz : ")
        musteri_veri_yonetimi.musteri_listele()
        musteri                 = input("Müşteri benzersiz kod giriniz : ")
        personel_veri_yonetimi.personel_listele()
        personel                = input("Personel benzersiz kod giriniz : ")
        fatura_tutari           = input("Araç benzersiz kod giriniz : ")
        fatura_tarihi           = datetime.now()
        fatura = fatura(fatura_benzersiz_kod, fatura_no, arac, musteri, personel, fatura_tutari, fatura_tarihi)

        sonuc = fatura_yonetimi.fatura_ekle(fatura)

        if sonuc[0] == False:
            print(sonuc[1])
            __fatura_ekle(fatura)
        else:
            print("Fatura başarıyla kaydedildi.") 
    
    else:
        print("Daha önce girdiğiniz değeri kabul etmek için enter tuşuna basınız.")
        fatura_no           = input(f"Fatura no giriniz ({fatura.no}) : ")
        arac_veri_yonetimi.arac_listele()
        arac                    = input("Araç benzersiz kod giriniz : ")
        musteri_veri_yonetimi.musteri_listele()
        musteri                 = input("Müşteri benzersiz kod giriniz : ")
        personel_veri_yonetimi.personel_listele()
        personel                = input("Personel benzersiz kod giriniz : ")
        fatura_tutari       = input(f"Fatura adresini giriniz ({fatura.tutar}) : ")
        fatura_tarihi       = input(f"Fatura telefonunu giriniz ({fatura.tarih}) : ")

        if fatura_no == "":
            fatura_no = fatura.no
        
        if arac == "":
            arac = fatura.arac

        if musteri == "":
            musteri = fatura.musteri
            
        if personel == "":
            personel = fatura.personel
        
        if fatura_tutari == "":
            fatura_tutari = fatura.tutar
        
        if fatura_tarihi == "":
            fatura_tarihi = fatura.tarih

        fatura = fatura(fatura.benzersiz_kod, fatura_no, arac, musteri, personel, fatura_tutari, fatura_tarihi)

        sonuc = fatura_yonetimi.fatura_ekle(fatura)

        if sonuc[0] == False:
            print(sonuc[1])
            __fatura_ekle(fatura)
        else:
            print("Fatura başarıyla kaydedildi.") 

def menu_getir(): 
    while True:
        print(menu_metni)
        secenek = int(input("Fatura menu seçiminizi yapınız: "))
        if secenek == 1:
            print("Fatura ekleme çalışıyor")
            __fatura_ekle(None)
        elif secenek == 2:
            fatura_listesi = fatura_yonetimi.fatura_listele()
            for fatura in fatura_listesi.items():
                print(fatura)
        elif secenek == 3:
            fatura_listesi = fatura_yonetimi.fatura_listele()
        elif secenek == 4:
            # fatura_menu_yonetimi.menu_getir()
            pass
        elif secenek == 5:
            # menu_yonetimi.ana_menu_getir()
            pass
        else:
            print("Lütfen doğru seçeneği seçiniz!")            
            