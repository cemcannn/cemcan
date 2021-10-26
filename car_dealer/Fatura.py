import os
from typing import Callable
from Arac import *
from Insan import *
from datetime import datetime

class Fatura:
    def __init__(self):
        self.fatura_listesi = {}
    
    def fatura_ekle(self,fatura_no:int,musteri:Musteri,arac:Arac,personel:Personel,fatura_tarihi:Callable, fatura_tutari:float):
        self.fatura_listesi[fatura_no]= [musteri,arac,personel,fatura_tarihi,fatura_tutari]  
        print("Fatura kaydedildi...")

    def faturalari_listele(self): 
        print("============== Liste ================")
        for h in self.fatura_listesi:
            print(h)
    
    def fatura_sil(self,fatura_no:int):
        self.fatura_listesi.pop(fatura_no)
        print("Fatura silindi...")

    # def fatura_tutari_hesapla(self,fatura_no:int,fatura_tutari:float) -> float:
    #     self.fatura_listesi[fatura_no]=fatura_tutari * 120 / 100

    def fatura_bul(self,fatura_no:int):
        print(f"Müşteri : {self.fatura_listesi[fatura_no][0]} | Araç  : {self.fatura_listesi[fatura_no][1]} | Satış Personeli : {self.fatura_listesi[fatura_no][2]} | Fatura Tarihi : {self.fatura_listesi[fatura_no][3]} | Fatura Tutarı : {self.fatura_listesi[fatura_no][4] }")

    def fatura_duzenle(self):
        fatura_no = input("Fatura numarası giriniz :")
        self.fatura_bul(fatura_no)
        duzenlenen = int(input("""
        Lütfen düzenlemek istediğiniz bilgiyi seçiniz :
        (0) Müşteri bilgileri        
        (1) Araç bilgileri
        (2) Personel bilgileri     
        (3) Fatura tarihi          
        (4) Fatura tutarı      
   
        """))
        self.fatura_listesi[fatura_no][duzenlenen] = input(f"Lütfen yeni düzenlemeyi giriniz : ")

fatura = Fatura()

class Fatura_Yonetim_Sistemi:
    def fatura_yonetim_sistemi():
        while True:
            os.system("cls")            
            print("""
            ===========================
            Fatura Yönetim Menüsü
            ===========================
            Lütfen bir seçenek seçiniz:
            (1) Fatura ekle
            (2) Fatura bul
            (3) Fatura sil
            (4) Fatura düzenle
            (5) Ana menüye dön
            ===========================
            """)
            secenek=input("Lütfen seçiminizi giriniz : ")
            if secenek=="1":
                os.system("cls")  
                if arac.arac_listesi=={}:
                    print("Henüz eklenmiş bir araç bulunmamaktadır! Lütfen önce araç yönetim menüsünden araç ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                elif personel.personel_listesi=={}:
                    print("Henüz eklenmiş bir personel bulunmamaktadır! Lütfen önce personel yönetim menüsünden personel ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")                
                elif musteri.musteri_listesi=={}:
                    print("Henüz eklenmiş bir müşteri bulunmamaktadır! Lütfen önce müşteri yönetim menüsünden müşteri ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:                
                    fatura_no=input("Fatura numarasını giriniz : ")
                    musteri.musteri_listele()
                    while 1==1:
                        try:
                            musteri_ekle = musteri.musteri_listesi[input("Listeden müşteri TCKN'si giriniz :")]
                            input("Devam etmek için bir tuşa basınız...")
                            break
                        except KeyError:
                            print("Lütfen doğru müşteri tckn si giriniz!","\a")     

                    arac.araclari_listele()
                    while 1==1:
                        try:
                            arac_ekle = arac.arac_listesi[input("Listeden araç kodu giriniz :")]
                            arac_tutari=float(arac_ekle[4]) * 120 /100
                            input("Devam etmek için bir tuşa basınız...")
                            break 
                        except KeyError:
                            print("Lütfen doğru araç kodu giriniz!","\a")                                       

                    personel.personel_listele()
                    while 1==1:
                        try:
                            personel_ekle = personel.personel_listesi[input("Listeden personel TCKN'si giriniz :")]
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru personel tckn si giriniz!","\a")  

                    fatura.fatura_ekle(fatura_no, musteri_ekle, arac_ekle, personel_ekle,datetime.now(),arac_tutari)
                    print(fatura.fatura_listesi)

            elif secenek=="2":
                os.system("cls")  
                if fatura.fatura_listesi=={}:
                    print("Henüz eklenmiş bir fatura bulunmamaktadır! Lütfen önce fatura ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")    
                else:
                    while 1==1:
                        try:
                            fatura.faturalari_listele()    
                            fatura.fatura_bul(input("Fatura kodunu giriniz : "))
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru fatura numarası giriniz!","\a")                     
                            fatura.faturalari_listele()                                               
            elif secenek=="3":
                os.system("cls")  
                if fatura.fatura_listesi=={}:
                    print("Henüz eklenmiş bir fatura bulunmamaktadır! Lütfen önce fatura ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")    
                else:
                    while 1==1:
                        try:
                            fatura.faturalari_listele()    
                            fatura.fatura_sil(input("Fatura kodunu giriniz : "))
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru fatura numarası giriniz!","\a")                     
                            fatura.faturalari_listele()     
            elif secenek=="4":
                os.system("cls")  
                if fatura.fatura_listesi=={}:
                    print("Henüz eklenmiş bir fatura bulunmamaktadır! Lütfen önce fatura ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:
                    while 1==1:
                        try:
                            fatura.faturalari_listele()    
                            fatura.fatura_duzenle()
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru fatura numarası giriniz!","\a") 
            elif secenek=="5":
                break
            else:
                print("""Lütfen doğru seçeneği seçiniz! ""","\a")
                input("Devam etmek için enter tuşuna basınız.")
