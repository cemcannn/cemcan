import os


class Insan:
    def __init__(self,tckn:int,adi:str,soyadi:str,adres:complex,il:str,ilce:str,tel:int):
        self.tckn = tckn
        self.adi = adi
        self.soyadi = soyadi
        self.adres = adres
        self.il = il
        self.ilce = ilce
        self.tel = tel
    
class Musteri(Insan):
    def __init__(self):
        self.musteri_listesi = {}

    def musteri_listele(self): 
        print("============== Liste ================")
        for h in self.musteri_listesi:
            print(h)

    def musteri_ekle(self, tckn:int,adi:str,soyadi:str,adres:str,il:str,ilce:str,tel:int ):
        self.musteri_listesi[tckn]=[adi,soyadi,adres,il,ilce,tel]
        print("Müşteri kaydedildi...")

    def musteri_listele(self): 
        print("============== Liste ================")
        for h in self.musteri_listesi:
            print(h)
    
    def musteri_sil(self,tckn:int):
        self.musteri_listesi.pop(tckn)
        print("Müşteri silindi...")

    def musteri_bul(self,tckn:int):
        print(f"Müşteri Adı: {self.musteri_listesi[tckn][0]} | Müşteri Soyadı : {self.musteri_listesi[tckn][1]} | Müşteri Adresi : {self.musteri_listesi[tckn][2]} | Müşteri İli : {self.musteri_listesi[tckn][3]} | Müşteri İlçesi : {self.musteri_listesi[tckn][4]} | Müşteri Telefonu : {self.musteri_listesi[tckn][5]} ")

    def musteri_duzenle(self):
        tckn = input("TCKN giriniz :")
        self.musteri_bul(tckn)
        duzenlenen = int(input("""
        Lütfen düzenlemek istediğiniz bilgiyi seçiniz :
        (0) Müşteri adı        
        (1) Müşteri soyadı     
        (2) Müşteri adresi     
        (3) Müşteri ili        
        (4) Müşteri ilçesi     
        (5) Müşteri telefonu   
        (6) Müşteri görevi     
        """))
        self.musteri_listesi[tckn][duzenlenen] = input(f"Lütfen yeni düzenlemeyi giriniz : ")

class Personel(Insan):
    def __init__(self):
        self.personel_listesi = {}

    def personel_ekle(self, tckn:int,adi:str,soyadi:str,adres:complex,il:str,ilce:str,tel:int,gorevi:str ):
        self.personel_listesi[tckn]=[adi,soyadi,adres,il,ilce,tel,gorevi]
        print("Personel kaydedildi...")

    def personel_listele(self): 
        print("============== Liste ================")
        for h in self.personel_listesi:
            print(h)

    def personel_sil(self,tckn:int):
        self.personel_listesi.pop(tckn)
        print("Personel silindi...")

    def personel_bul(self,tckn:int):
        print(f"Personel Adı: {self.personel_listesi[tckn][0]} | Personel Soyadı : {self.personel_listesi[tckn][1]} | Personel Adresi : {self.personel_listesi[tckn][2]} | Personel İli : {self.personel_listesi[tckn][3]} | Personel İlçesi : {self.personel_listesi[tckn][4]} | Personel Telefonu : {self.personel_listesi[tckn][5]}, | Personel Görevi : {self.personel_listesi[tckn][6]} ")

    def personel_duzenle(self):
        tckn = input("TCKN giriniz :")
        self.personel_bul(tckn)
        duzenlenen = int(input("""
        Lütfen düzenlemek istediğiniz bilgiyi seçiniz :
        (0) Personel adı        
        (1) Personel soyadı     
        (2) Personel adresi     
        (3) Personel ili        
        (4) Personel ilçesi     
        (5) Personel telefonu   
        (6) Personel görevi     
        """))
        self.personel_listesi[tckn][duzenlenen] = input(f"Lütfen yeni düzenlemeyi giriniz : ")

musteri = Musteri()

class Musteri_Yonetim_Sistemi:
    def musteri_yonetim_sistemi():
        while True:
            os.system("cls")            
            print("""
            ===========================
            Müşteri Yönetim Menüsü
            ===========================
            Lütfen bir seçenek seçiniz:
            (1) Müşteri ekle
            (2) Müşteri bul
            (3) Müşteri sil
            (4) Müşteri düzenle
            (5) Ana menüye dön
            ===========================
            """)
            secenek=input("Lütfen seçiminizi giriniz : ")
            if secenek=="1":
                os.system("cls")
                musteri.musteri_ekle(input("TCKN giriniz : "), input("Müşteri adını giriniz : "), input("Müşteri soyadını giriniz : "), input("Müşteri adresini giriniz : "), input("Müşteri ilini giriniz : "), input("Müşteri ilçesini giriniz : "), input("Müşteri telefonunu giriniz : "))
                input("Devam etmek için bir tuşa basınız")            
            elif secenek=="2":
                os.system("cls")                
                if musteri.musteri_listesi=={}:
                    print("Henüz eklenmiş bir müşteri bulunmamaktadır! Lütfen önce müşteri ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:
                    while 1==1:
                        try:
                            musteri.musteri_listele()
                            musteri.musteri_bul(input("TCKN giriniz : "))
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru müşteri tckn si giriniz!","\a")  
                
            elif secenek=="3":
                os.system("cls")  
                if musteri.musteri_listesi=={}:
                    print("Henüz eklenmiş bir müşteri bulunmamaktadır! Lütfen önce müşteri ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:
                    while 1==1:
                        try:       
                            musteri.musteri_listele()         
                            musteri.musteri_sil(input("TCKN giriniz : "))
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru müşteri tckn si giriniz!","\a")  
                
            elif secenek=="4":
                os.system("cls")  
                if musteri.musteri_listesi=={}:
                    print("Henüz eklenmiş bir müşteri bulunmamaktadır! Lütfen önce müşteri ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:
                    while 1==1:
                        try:
                            musteri.musteri_listele()
                            musteri.musteri_duzenle()
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru müşteri tckn si giriniz!","\a") 
            elif secenek=="5":
                break
            else:
                os.system("cls")
                print("""Lütfen doğru seçeneği seçiniz! ""","\a")
                input("Devam etmek için enter tuşuna basınız.")

personel = Personel()

class Personel_Yonetim_Sistemi:
    def personel_yonetim_sistemi():
        while True:
            os.system("cls")
            print("""
            ===========================
            Personel Yönetim Menüsü
            ===========================
            Lütfen bir seçenek seçiniz:
            (1) Personel ekle
            (2) Personel bul
            (3) Personel sil
            (4) Personel düzenle
            (5) Ana menüye dön
            ===========================
            """)
            secenek=input("Lütfen seçiminizi giriniz : ")
            if secenek=="1":
                os.system("cls")
                personel.personel_ekle(input("TCKN giriniz : "), input("Personel adını giriniz : "), input("Personel soyadını giriniz : "), input("Personel adresini giriniz : "), input("Personel ilini giriniz : "), input("Personel ilçesini giriniz : "), input("Personel telefonunu giriniz : "), input("Personel görevini giriniz : "))
                input("Devam etmek için bir tuşa basınız")                
            elif secenek=="2":
                os.system("cls")  
                if personel.personel_listesi=={}:
                    print("Henüz eklenmiş bir personel bulunmamaktadır! Lütfen önce personel ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:
                    while 1==1:
                        try:
                            personel.personel_listele()
                            personel.personel_bul(input("TCKN giriniz : "))
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru personel tckn si giriniz!","\a")  
            elif secenek=="3":
                os.system("cls")  
                if personel.personel_listesi=={}:
                    print("Henüz eklenmiş bir personel bulunmamaktadır! Lütfen önce personel ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")                
                else:
                    while 1==1:
                        try:          
                            personel.personel_listele()      
                            personel.personel_sil(input("TCKN giriniz : "))
                            input("Devam etmek için bir tuşa basınız") 
                            break    
                        except KeyError:
                            print("Lütfen doğru personel tckn si giriniz!","\a")             
            elif secenek=="4":
                os.system("cls")  
                if personel.personel_listesi=={}:
                    print("Henüz eklenmiş bir personel bulunmamaktadır! Lütfen önce personel ekleyiniz.","\a")
                    input("Devam etmek için bir tuşa basınız")
                else:
                    while 1==1:
                        try:
                            personel.personel_listele()
                            personel.personel_duzenle()
                            input("Devam etmek için bir tuşa basınız")
                            break
                        except KeyError:
                            print("Lütfen doğru personel tckn si giriniz!","\a") 
            elif secenek=="5":
                break
            else:
                print("""Lütfen doğru seçeneği seçiniz! """)
                input("Devam etmek için enter tuşuna basınız.")