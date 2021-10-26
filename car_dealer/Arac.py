import os

class Arac:
    def __init__(self):
        self.arac_listesi = {}
    
    def arac_ekle(self, arac_kodu:int, arac_markasi:str, arac_modeli:str, arac_yili:int, arac_kategorisi:str, arac_fiyati:float, arac_rengi:str):
        self.arac_listesi[arac_kodu]=[arac_markasi,arac_modeli,arac_yili,arac_kategorisi,arac_fiyati,arac_rengi]
        print("Araç kaydedildi...")
        
    def araclari_listele(self): 
        print("============== Liste ================")
        for h in self.arac_listesi:
            print(h)
    
    def arac_sil(self,arac_kodu:int):
        self.arac_listesi.pop(arac_kodu)
        print("Araç silindi...")

    def arac_bul(self,arac_kodu:int):
        print(f"Araç Markası: {self.arac_listesi[arac_kodu][0]} | Araç Modeli : {self.arac_listesi[arac_kodu][1]} | Araç Yılı : {self.arac_listesi[arac_kodu][2]} | Araç Kategorisi : {self.arac_listesi[arac_kodu][3]} | Araç Fiyatı : {self.arac_listesi[arac_kodu][4]} | Araç Rengi : {self.arac_listesi[arac_kodu][5]}")

    def arac_duzenle(self):
        arac_kodu = input("Araç kodu giriniz :")
        self.arac_bul(arac_kodu)
        duzenlenen = int(input("""
        Lütfen düzenlemek istediğiniz bilgiyi seçiniz :
        (0) Araç markası        
        (1) Araç modeli     
        (2) Araç yılı     
        (3) Araç kategorisi        
        (4) Araç fiyatı     
        (5) Araç rengi   
        """))
        self.arac_listesi[arac_kodu][duzenlenen] = input(f"Lütfen yeni düzenlemeyi giriniz : ")

arac = Arac()      

class Arac_Yonetim_Sistemi:
    def arac_yonetim_sistemi():
        while True:
            os.system("cls")            
            print("""
            ===========================
            Araç Yönetim Menüsü
            ===========================
            Lütfen bir seçenek seçiniz:
            (1) Araç ekle
            (2) Araç bul
            (3) Araç sil
            (4) Araç düzenle
            (5) Ana menüye dön
            ===========================
            """)
            secenek=input("Lütfen seçiminizi giriniz : ")
            if secenek=="1":
                os.system("cls")
                arac.arac_ekle(input("Araç kodunu giriniz : "), input("Araç markasını giriniz : "), input("Araç modelini giriniz : "), input("Araç yılını giriniz : "), input("Araç kategorisini giriniz : "), input("Araç fiyatını giriniz : "), input("Araç rengini giriniz : "))
                input("Devam etmek için bir tuşa basınız")
            elif secenek=="2":
                os.system("cls")
                if arac.arac_listesi=={}:
                    print("Henüz eklenmiş bir araç bulunmamaktadır! Lütfen önce araç ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:    
                    while 1==1:
                        try:
                            arac.araclari_listele()
                            arac.arac_bul(input("Araç kodunu giriniz : "))
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru araç kodunu giriniz!","\a")              
            elif secenek=="3":
                os.system("cls")
                if arac.arac_listesi=={}:
                    print("Henüz eklenmiş bir araç bulunmamaktadır! Lütfen önce araç ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:
                    while 1==1:
                        try:
                            arac.araclari_listele()
                            arac.arac_sil(input("Araç kodunu giriniz : "))
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru araç kodunu giriniz!","\a")     
            elif secenek=="4":
                os.system("cls")
                if arac.arac_listesi=={}:
                    print("Henüz eklenmiş bir araç bulunmamaktadır! Lütfen önce araç ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:
                    while 1==1:
                        try:
                            arac.araclari_listele()
                            arac.arac_duzenle()
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru araç kodunu giriniz!","\a")     

            elif secenek=="5":
                break
            else:
                print("""Lütfen doğru seçeneği seçiniz! """)
                input("Devam etmek için enter tuşuna basınız.")