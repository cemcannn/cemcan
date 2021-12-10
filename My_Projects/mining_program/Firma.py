import os
from Ruhsat import *

class Firma:
    def __init__(self):
        self.firma_listesi = {"4547":["45","elma","armut","ayva"]}
        
    def firma_ekle(self, vergi_kimlik_no:int, tckn:int, firma_ismi:str, yetkili_ismi:str, yetkili_soyismi:str):
        print("Lütfen şahıs için 'vergi kimlik numarası' bölümüne 'tckn' giriniz.")
        self.firma_listesi[vergi_kimlik_no]=[tckn,firma_ismi,yetkili_ismi,yetkili_soyismi]
        print("Firma/Şahıs kaydedildi...")
        
    def firma_listele(self): 
        print("============== Liste ================")
        for firma in self.firma_listesi:
            print(firma)
    
    def firma_sil(self,vergi_kimlik_no:int):
        self.firma_listesi.pop(vergi_kimlik_no)
        print("Firma silindi...")

    def firma_bul(self,vergi_kimlik_no:int):
        print(f"Firma yetkili tckn : {self.firma_listesi[vergi_kimlik_no][0]} | Firma ismi : {self.firma_listesi[vergi_kimlik_no][1]} | Firma yetkilisi ismi : {self.firma_listesi[vergi_kimlik_no][2]} | Firma yetkilisi soyismi : {self.firma_listesi[vergi_kimlik_no][3]} ")

    def firma_duzenle(self):
        vergi_kimlik_no = input("Firma vergi kimlik numarası giriniz :")
        self.firma_bul(vergi_kimlik_no)
        duzenlenen = int(input("""
        Lütfen düzenlemek istediğiniz bilgiyi seçiniz :
        (0) Firma yetkili tckn        
        (1) Firma ismi   
        (2) Firma yetkilisi ismi    
        (3) Firma yetkilisi soyismi    
        """))
        self.firma_listesi[vergi_kimlik_no][duzenlenen] = input(f"Lütfen yeni düzenlemeyi giriniz : ")

firma = Firma()      

class Firma_Yonetim_Sistemi:
    def firma_yonetim_sistemi():
        while True:
            os.system("cls")            
            print("""
            ===========================
            Firma Yönetim Menüsü
            ===========================
            Lütfen bir seçenek seçiniz:
            (1) Firma ekle
            (2) Firmaya ruhsat ekle
            (3) Firma bul
            (4) Firma sil
            (5) Firma düzenle
            (6) Ana menüye dön
            ===========================
            """)
            secenek=input("Lütfen seçiminizi giriniz : ")
            if secenek=="1":
                os.system("cls")
                firma.firma_ekle(input("Firma vergi kimlik numarası giriniz : "), input("Firma yetkili tckn giriniz : "), input("Firma ismi giriniz : "), input("Firma yetkili ismi giriniz : "), input("Firma yetkili soyismi giriniz : "))
                input("Devam etmek için bir tuşa basınız")
            elif secenek=="2":
                while 1==1:
                    if ruhsat.ruhsat_listesi=={}:
                        print("Henüz eklenmiş bir firma bulunmamaktadır! Lütfen önce firma yönetim menüsünden firma bilgilerini giriniz.","\a")
                        input("Devam etmek için bir tuşa basınız")
                        break
                    elif ruhsat.ruhsat_listesi=={}:
                        print("Henüz eklenmiş bir ruhsat bulunmamaktadır! Lütfen önce ruhsat yönetim menüsünden ruhsat bilgilerini giriniz.","\a")
                        input("Devam etmek için bir tuşa basınız")
                        break
                    else:
                        try:
                            firma.firma_listele()
                            ruhsat_eklenecek_firma= firma.firma_listesi[input("Lütfen ruhsat eklenecek firmanın vergi kimlik numarasını giriniz : ")]
                            ruhsat.ruhsat_listele()
                            firma_ruhsati = ruhsat.ruhsat_listesi[input("Lütfen ruhsatın erişim numarasını giriniz : ")]

                           # print(firma.firma_listesi[ruhsat_eklenecek_firma])

                            ruhsat_eklenecek_firma.append(firma_ruhsati)
                            print(firma.firma_listesi)
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru firma vergi kimlik numarası giriniz!","\a")
            elif secenek=="3":
                os.system("cls")
                if firma.firma_listesi=={}:
                    print("Henüz eklenmiş bir firma bulunmamaktadır! Lütfen önce firma ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:    
                    while 1==1:
                        try:
                            firma.firma_listele()
                            firma.firma_bul(input("Firma vergi kimlik numarası giriniz : "))
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru araç kodunu giriniz!","\a")              
            elif secenek=="4":
                os.system("cls")
                if firma.firma_listesi=={}:
                    print("Henüz eklenmiş bir firma bulunmamaktadır! Lütfen önce firma ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:
                    while 1==1:
                        try:
                            firma.firma_listele()
                            firma.firma_sil(input("Firma vergi kimlik numarası giriniz : "))
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru firma vergi kimlik numarası giriniz!","\a")     
            elif secenek=="5":
                os.system("cls")
                if firma.firma_listesi=={}:
                    print("Henüz eklenmiş bir firma bulunmamaktadır! Lütfen önce firma ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:
                    while 1==1:
                        try:
                            firma.firma_listele()
                            firma.firma_duzenle()
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru firma vergi kimlik numarası giriniz!","\a")  

            elif secenek=="6":
                break
            else:
                print("""Lütfen doğru seçeneği seçiniz! """)
                input("Devam etmek için enter tuşuna basınız.")
