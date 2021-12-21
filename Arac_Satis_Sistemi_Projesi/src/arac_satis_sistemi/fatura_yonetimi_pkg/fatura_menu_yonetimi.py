import menu_yonetimi
from arac_yonetimi_pkg import arac_veri_yonetimi as avy
from musteri_yonetimi_pkg import musteri_veri_yonetimi as mvy
from personel_yonetimi_pkg import personel_veri_yonetimi as pvy
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
        print(avy.arac_listele())
        fatura_arac                    = avy.arac_getir_benzersizkod(int(input("Araç benzersiz kod giriniz : ")))
        print(mvy.musteri_listele())
        fatura_musteri                 = mvy.musteri_getir_benzersizkod(int(input("Müşteri benzersiz kod giriniz : ")))
        print(pvy.personel_listele())
        fatura_personel                = pvy.personel_getir_benzersizkod(int(input("Personel benzersiz kod giriniz : ")))
        fatura_tutari           = fatura_yonetimi.__vergi_hesapla(fatura_arac)
        fatura_tarihi           = datetime.now()
        fatura = Fatura(fatura_benzersiz_kod, fatura_no, fatura_arac, fatura_musteri, fatura_personel, fatura_tutari, fatura_tarihi)

        sonuc = fatura_yonetimi.fatura_ekle(fatura)

        if sonuc[0] == False:
            print(sonuc[1])
            __fatura_ekle(fatura)
        else:
            print("Fatura başarıyla kaydedildi.") 
    
    else:
        print("Daha önce girdiğiniz değeri kabul etmek için enter tuşuna basınız.")
        fatura_no           = input(f"Fatura no giriniz ({fatura.no}) : ")
        print(avy.arac_listele())
        fatura_arac                    = avy.arac_getir_benzersizkod(int(input("Araç benzersiz kod giriniz ({fatura.arac}): ")))
        print(mvy.musteri_listele())
        fatura_musteri                 = mvy.musteri_getir_benzersizkod(int(input("Müşteri benzersiz kod giriniz ({fatura.musteri}): ")))
        print(pvy.personel_listele())
        fatura_personel                = pvy.personel_getir_benzersizkod(int(input("Personel benzersiz kod giriniz ({fatura.personel}): ")))
        fatura_tutari       = fatura_yonetimi.__vergi_hesapla(fatura_arac)
        fatura_tarihi       = datetime.now()

        if fatura_no == "":
            fatura_no = fatura.no
        
        if fatura_arac == "":
            fatura_arac = fatura.arac

        if fatura_musteri == "":
            fatura_musteri = fatura.musteri
            
        if fatura_personel == "":
            fatura_personel = fatura.personel
        
        if fatura_tutari == "":
            fatura_tutari = fatura.tutar
        
        if fatura_tarihi == "":
            fatura_tarihi = fatura.tarih

        fatura = Fatura(fatura.benzersiz_kod, fatura_no, fatura_arac, fatura_musteri, fatura_personel, fatura_tutari, fatura_tarihi)

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
            menu_yonetimi.ana_menu_getir()
        else:
            print("Lütfen doğru seçeneği seçiniz!")            
            