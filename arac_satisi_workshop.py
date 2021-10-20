import os
from datetime import datetime
from typing import Callable

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
        pass
        
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
        pass

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
        pass

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
        pass

class Ayar:
    def saat_ayari():
        print("Saat ve tarih ayarı yapıldı")

class Aciklama:
    def aciklama():
        print("""

        Araç satış sistemine hoşgeldiniz...

        Bu işlem araç satışı gerçekleştirmek için fatura kesmek üzere düzenlenmiştir.
        Fatura kesebilmek için öncelikle araç bilgileri, müşteri bilgilier ve personel bilgilerini girmeniz gerekmektedir.

        Araç bilgilerini girmek için ana menüden 1 numaralı araç yönetim menüsüne girmeniz gerekmektedir. Araç yönetim menüsünde 
        5 adet seçenek bulunmaktadır. 1. seçenekten araç ekleme, 2. seçenekten araç bulma, 3. seçenekten araç silme, 4. seçenekten 
        araç düzenleme yapabilir ve 5. seçenekten ana menüye dönebilirsiniz. Araç eklemek için araç kodu, araç markası, araç modeli, 
        araç yılı, araç kategorisi, araç fiyatı ve araç rengi bilgileri gerekmektedir. Bu bilgileri ekrana girdikten sonra aracınız 
        listeye eklenecektir. Araç  bulma ekranında ekrana gelen listeden araç kodunu girerek araç bilgilerine erişebilirsiniz. 
        Araç silme ekranında yine ekrana gelen listeden araç kodunu girerek ilgili aracı listeden silebilirsiniz fakat faturası 
        kesilmiş araç listeden silinmez. Araç düzenle ekranında yine listeden araç kodunu girerek ilgili aracın bilgilerini 
        düzenleyebilirsiniz.

        Müşteri bilgilerini girmek için ana menüden 2 numaralı müşteri yönetim menüsüne girmeniz gerekmektedir. Müşteri yönetim 
        menüsünde 5 adet seçenek bulunmaktadır. 1. seçenekten müşteri ekleme, 2. seçenekten müşteri bulma, 3. seçenekten müşteri silme, 
        4. seçenekten müşteri düzenleme yapabilir ve 5. seçenekten ana menüye dönebilirsiniz. Müşteri eklemek için müşteri TCKN, müşteri 
        adı, müşteri soyadı, müşteri adresi, müşteri ili, müşteri ilçesi ve müşteri telefon bilgileri gerekmektedir. Bu bilgileri ekrana 
        girdikten sonra müşteri listeye eklenecektir. Müşteri  bulma ekranında ekrana gelen listeden müşteri TCKN girerek müşteri 
        bilgilerine erişebilirsiniz. Müşteri silme ekranında yine ekrana gelen listeden müşteri TCKN girerek ilgili müşteriyi listeden 
        silebilirsiniz fakat faturası kesilmiş müşteri bilgileri listeden silinmez. Müşteri düzenle ekranında yine listeden müşteri TCKN 
        girerek ilgili aracın bilgilerini düzenleyebilirsiniz.        
        
        Personel bilgilerini girmek için ana menüden 3 numaralı personel yönetim menüsüne girmeniz gerekmektedir. Personel yönetim 
        menüsünde 5 adet seçenek bulunmaktadır. 1. seçenekten personel ekleme, 2. seçenekten personel bulma, 3. seçenekten personel silme, 
        4. seçenekten personel düzenleme yapabilir ve 5. seçenekten ana menüye dönebilirsiniz. Personel eklemek için müşteri TCKN, 
        personel adı, personel soyadı, personel adresi, personel ili, personel ilçesi, personel telefonu ve personel görev bilgileri 
        gerekmektedir. Bu bilgileri ekrana girdikten sonra personel listeye eklenecektir. Personel  bulma ekranında ekrana gelen listeden 
        personel TCKN girerek personel bilgilerine erişebilirsiniz. Personel silme ekranında yine ekrana gelen listeden personel TCKN 
        girerek ilgili personeli listeden silebilirsiniz fakat faturası kesilmiş personel bilgileri listeden silinmez. Personel düzenle 
        ekranında yine listeden personel TCKN girerek ilgili aracın bilgilerini düzenleyebilirsiniz.         
        
        Fatura bilgilerini girmek için ana menüden 4 numaralı fatura yönetim menüsüne girmeniz gerekmektedir. Fatura yönetim menüsünde 
        5 adet seçenek bulunmaktadır. 1. seçenekten fatura ekleme, 2. seçenekten fatura bulma, 3. seçenekten fatura silme, 4. seçenekten 
        fatura düzenleme yapabilir ve 5. seçenekten ana menüye dönebilirsiniz. Fatura eklemek için fatura numarası, fatura kesilecek 
        müşteri TCKN'si, fatura kesilecek araç kodu ve fatura kesecek personel bilgileri gerekmektedir. Bu bilgilerden fatura numarası 
        ekrana girildikten sırayla sistem müşteri listesini ekrana verecek, listeden fatura kesilecek müşterinin TCKN'sini girmenizi 
        isteyecek, sonrasında araç listesini ekrana verecek, listeden satılacak aracın araç kodunu girmenizi isteyecek, son olarak personel 
        listesini ekrana verecek, listeden fatura kesecek personel TCKN'sini ekrana girmenizi isteyecek ve fatura kesilerek sisteme kayıt 
        edilecektir. Fatura  bulma ekranında ekrana gelen listeden fatura numarası girerek fatura bilgilerine erişebilirsiniz. Fatura silme 
        ekranında yine ekrana gelen listeden fatura numarası girerek ilgili faturayı listeden silebilirsiniz. Fatura düzenle ekranında yine 
        listeden fatura numarsı girerek ilgili fatura bilgilerini düzenleyebilirsiniz.

        Ana menüden 6. seçeneği seçmeniz durumunda saat ve tarih ayarlarını yapabilirsiniz.

        Ana menüden 7. seçeneği seçmeniz durumunda ise sistemden çıkış yapabilirsiniz.      

        """)

fatura = Fatura()
arac = Arac()
musteri = Musteri()
personel = Personel()

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
                arac.arac_ekle(input("Araç kodunu giriniz : "), input("Araç markasını giriniz : "), input("Araç modelini giriniz : "), input("Araç yılını giriniz : "), input("Araç kategorisini giriniz : "), input("Araç fiyatını giriniz : "), input("Araç rengini giriniz : "))
                print(arac.arac_listesi)
                input("Devam etmek için bir tuşa basınız")
            elif secenek=="2":
                arac.araclari_listele()
                arac.arac_bul(input("Araç kodunu giriniz : "))
                input("Devam etmek için bir tuşa basınız")
            elif secenek=="3":
                arac.araclari_listele()
                arac.arac_sil(input("Araç kodunu giriniz : "))
                input("Devam etmek için bir tuşa basınız")
            elif secenek=="4":
                arac.arac_duzenle()
            elif secenek=="5":
                break
            else:
                os.system("cls")
                print("""Lütfen doğru seçeneği seçiniz! """)
                input("Devam etmek için enter tuşuna basınız.")

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

                fatura_no=input("Fatura numarasını giriniz : ")

                musteri.musteri_listele()
                while 1==1:
                    try:
                        musteri_ekle = musteri.musteri_listesi[input("Listeden müşteri TCKN'si giriniz :")]
                        input("Devam etmek için bir tuşa basınız...")
                        break
                    except KeyError:
                        print("Lütfen doğru müşteri tckn si giriniz!")     

                arac.araclari_listele()
                while 1==1:
                    try:
                        arac_ekle = arac.arac_listesi[input("Listeden araç kodu giriniz :")]
                        arac_tutari=float(arac_ekle[4]) * 120 /100
                        input("Devam etmek için bir tuşa basınız...")
                        break 
                    except KeyError:
                        print("Lütfen doğru araç kodu giriniz!")                                       

                personel.personel_listele()
                while 1==1:
                    try:
                        personel_ekle = personel.personel_listesi[input("Listeden personel TCKN'si giriniz :")]
                        input("Devam etmek için bir tuşa basınız")
                        break
                    except KeyError:
                        print("Lütfen doğru personel tckn si giriniz!")  

                fatura.fatura_ekle(fatura_no, musteri_ekle, arac_ekle, personel_ekle,datetime.now(),arac_tutari)
                print(fatura.fatura_listesi)

            elif secenek=="2":
                fatura.faturalari_listele()
                fatura.fatura_bul(input("Fatura kodunu giriniz : "))
            elif secenek=="3":
                fatura.faturalari_listele()
                fatura.fatura_sil(input("Fatura kodunu giriniz : "))
            elif secenek=="4":
                fatura.fatura_duzenle()
            elif secenek=="5":
                break
            else:
                os.system("cls")
                print("""Lütfen doğru seçeneği seçiniz! """)
                input("Devam etmek için enter tuşuna basınız.")

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
                musteri.musteri_ekle(input("TCKN giriniz : "), input("Müşteri adını giriniz : "), input("Müşteri soyadını giriniz : "), input("Müşteri adresini giriniz : "), input("Müşteri ilini giriniz : "), input("Müşteri ilçesini giriniz : "), input("Müşteri telefonunu giriniz : "))
                input("Devam etmek için bir tuşa basınız")            
            elif secenek=="2":
                musteri.musteri_listele()
                musteri.musteri_bul(input("TCKN giriniz : "))
                input("Devam etmek için bir tuşa basınız")            
            elif secenek=="3":
                musteri.musteri_listele()
                musteri.musteri_sil(input("TCKN giriniz : "))
                input("Devam etmek için bir tuşa basınız")                
            elif secenek=="4":
                musteri.musteri_duzenle()
            elif secenek=="5":
                break
            else:
                os.system("cls")
                print("""Lütfen doğru seçeneği seçiniz! """)
                input("Devam etmek için enter tuşuna basınız.")

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
                personel.personel_ekle(input("TCKN giriniz : "), input("Personel adını giriniz : "), input("Personel soyadını giriniz : "), input("Personel adresini giriniz : "), input("Personel ilini giriniz : "), input("Personel ilçesini giriniz : "), input("Personel telefonunu giriniz : "), input("Personel görevini giriniz : "))
                input("Devam etmek için bir tuşa basınız")                
            elif secenek=="2":
                personel.personel_listele()
                personel.personel_bul(input("TCKN giriniz : "))
                input("Devam etmek için bir tuşa basınız")
            elif secenek=="3":
                personel.personel_listele()
                personel.personel_sil(input("TCKN giriniz : "))
                input("Devam etmek için bir tuşa basınız")                
            elif secenek=="4":
                personel.personel_duzenle()
            elif secenek=="5":
                break
            else:
                os.system("cls")
                print("""Lütfen doğru seçeneği seçiniz! """)
                input("Devam etmek için enter tuşuna basınız.")

class Menu_Yonetimi:
    def menu_yonetimi():
        input("Hoşgeldiniz. Devam etmek için bir tuşa basınız")
        while True:
            os.system("cls")
            print("""
            ===========================
            Ana Menü
            ===========================
            Lütfen bir seçenek seçiniz:
            (1) Araç yönetimi
            (2) Müşteri yönetimi
            (3) Personel yönetimi
            (4) Fatura yönetimi
            (5) Yardım
            (6) Saat/tarih ayarı
            (7) Çıkış
            ===========================
            """)
            secenek=input("Lütfen seçiminizi giriniz : ")   
            if secenek=="1":
                Arac_Yonetim_Sistemi.arac_yonetim_sistemi()
            elif secenek=="2":
                Musteri_Yonetim_Sistemi.musteri_yonetim_sistemi()
            elif secenek=="3":
                Personel_Yonetim_Sistemi.personel_yonetim_sistemi()
            elif secenek=="4":
                Fatura_Yonetim_Sistemi.fatura_yonetim_sistemi()
            elif secenek=="5":
                os.system("cls")
                Aciklama.aciklama()
                input("Devam etmek için enter tuşuna basınız.")            
            elif secenek=="6":
                os.system("cls")
                Ayar.saat_ayari()
                input("Devam etmek için enter tuşuna basınız.")             
            elif secenek=="7":
                os.system("cls")
                print("""
                ======================
                
                Güle güle...
                
                ======================
                """)
                input("")
                break

            else:
                os.system("cls")
                print("""Lütfen doğru seçeneği seçiniz! """)
                input("Devam etmek için enter tuşuna basınız.")


Menu_Yonetimi.menu_yonetimi()
