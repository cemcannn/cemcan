import os

class Ruhsat:
    def __init__(self):
        self.ruhsat_listesi = {"3455986":["20128000","2-b","mermer","genel aram dönemi","2010","2020","ankara","etimesgut","akay","20.5"]}

    def ruhsat_ekle(self,erisim_no:int, sicil_no:int , grubu:complex, maden_cinsi:str, donemi:str, ruhsat_baslangic_tarihi:int, ruhsat_bitis_tarihi:int, il:str, ilce:str, koy_mahalle:str, alan:float, ):
        self.ruhsat_listesi[erisim_no]=[sicil_no,grubu,maden_cinsi, donemi,ruhsat_baslangic_tarihi,ruhsat_bitis_tarihi,il,ilce,koy_mahalle,alan]
        print("Ruhsat kaydedildi...")
        
    def ruhsat_listele(self): 
        print("============== Liste ================")
        for ruhsat in self.ruhsat_listesi:
            print(ruhsat)
    
    def ruhsat_sil(self,erisim_no:int):
        self.ruhsat_listesi.pop(erisim_no)
        print(f"{erisim_no} erişim numaralı ruhsat silindi...")

    def ruhsat_getir(self, erisim_no:int):
        print(f"Ruhsat sicil numarası : {self.ruhsat_listesi[erisim_no][0]} | Ruhsat grubu : {self.ruhsat_listesi[erisim_no][1]} | Ruhsat maden cinsi : {self.ruhsat_listesi[erisim_no][2]} | Ruhsat dönemi : {self.ruhsat_listesi[erisim_no][3]} | Ruhsat başlangıç tarihi : {self.ruhsat_listesi[erisim_no][4]} | Ruhsat bitiş tarihi : {self.ruhsat_listesi[erisim_no][5]} | Ruhsat ili : {self.ruhsat_listesi[erisim_no][6]} | Ruhsat ilçesi : {self.ruhsat_listesi[erisim_no][7]} | Ruhsat koy/mahalle : {self.ruhsat_listesi[erisim_no][8]} | Ruhsat alanı : {self.ruhsat_listesi[erisim_no][9]}")

    def ruhsat_duzenle(self):
        erisim_no = input("Ruhsat erişim numarası giriniz :")
        self.ruhsat_getir(erisim_no)
        duzenlenen = int(input("""
        Lütfen düzenlemek istediğiniz bilgiyi seçiniz :
        (0)  Ruhsat sicil numarası        
        (1)  Ruhsat grubu
        (2)  Ruhsat maden cinsi    
        (3)  Ruhsat dönemi
        (4)  Ruhsat başlangıç tarihi
        (5)  Ruhsat bitiş tarihi
        (6)  Ruhsat ili
        (7)  Ruhsat ilçesi
        (8)  Ruhsat koy/mahalle
        (9)  Ruhsat alanı    
        (10) Ruhsat sahibi
        """))
        self.ruhsat_listesi[erisim_no][duzenlenen] = input(f"Lütfen yeni düzenlemeyi giriniz : ")

ruhsat = Ruhsat()      

class Ruhsat_Yonetim_Sistemi:
    def ruhsat_yonetim_sistemi():
        while True:
            os.system("cls")            
            print("""
            ===========================
            Ruhsat Yönetim Menüsü
            ===========================
            Lütfen bir seçenek seçiniz:
            (1) Ruhsat ekle
            (2) Ruhsat bul
            (3) Ruhsat sil
            (4) Ruhsat düzenle
            (5) Ana menüye dön
            ===========================
            """)
            secenek=input("Lütfen seçiminizi giriniz : ")
            if secenek=="1":
                os.system("cls")
                ruhsat.ruhsat_ekle(input("Ruhsatın erişim numarasını giriniz : "), input("Ruhsatın sicil numarasını giriniz : "), input("Ruhsatın gurubunu giriniz : "), input("Ruhsatın maden cinsini giriniz : "), input("Ruhsatın dönemini giriniz : "), input("Ruhsatın başlangıç tarihini giriniz : "), input("Ruhsatın bitiş tarihini giriniz : "), input("Ruhsatın ilini giriniz : "), input("Ruhsatın ilçesini giriniz : "), input("Ruhsatın bulunduğu koy/mahalle giriniz : "), input("Ruhsatın alanını giriniz : "))
                input("Devam etmek için bir tuşa basınız")
            elif secenek=="2":
                os.system("cls")
                if ruhsat.ruhsat_listesi=={}:
                    print("Henüz eklenmiş bir ruhsat bulunmamaktadır! Lütfen önce ruhsat ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:    
                    while 1==1:
                        try:
                            ruhsat.ruhsat_listele()
                            ruhsat.ruhsat_getir(input("Ruhsatın erişim numarasını giriniz : "))
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru erişim numarasını giriniz!","\a")              
            elif secenek=="3":
                os.system("cls")
                if ruhsat.ruhsat_listesi=={}:
                    print("Henüz eklenmiş bir ruhsat bulunmamaktadır! Lütfen önce ruhsat ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:
                    while 1==1:
                        try:
                            ruhsat.ruhsat_listele()
                            ruhsat.ruhsat_sil(input("Ruhsatın erişim numarasını giriniz : "))
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru erişim numarası giriniz!","\a")     
            elif secenek=="4":
                os.system("cls")
                if ruhsat.ruhsat_listesi=={}:
                    print("Henüz eklenmiş bir ruhsat bulunmamaktadır! Lütfen önce ruhsat ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:
                    while 1==1:
                        try:
                            ruhsat.ruhsat_listele()
                            ruhsat.ruhsat_duzenle()
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru erişim numarası giriniz!","\a")     

            elif secenek=="5":
                break
            else:
                print("""Lütfen doğru seçeneği seçiniz! """)
                input("Devam etmek için enter tuşuna basınız.")
