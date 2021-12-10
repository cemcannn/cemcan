## Inheritance (Kalıtım)

class BilgisayarMuhendisi:
    def __init__(self, isim:str, boy:int, kilo:int):
        self.isim= isim
        self.boy = boy
        self.kilo = kilo

    def yuru(self, adim_sayisi:int):
        print(str(adim_sayisi) + "adım yürüdü")

    def uyu(self):
        print("uyudu")

    def toplantiya_katil(self):
        print("toplantıya katıldı")

    def hesap_yap(self):
        print("hesap yap")
    
    def kod_yaz(self):
        print("kod yazıldı")

class InsaatMuhendisi:
    def __init__(self, isim:str, boy:int, kilo:int):
        self.isim= isim
        self.boy = boy
        self.kilo = kilo

    def yuru(self, adim_sayisi:int):
        print(str(adim_sayisi) + "adım yürüdü")

    def uyu(self):
        print("uyudu")

    def toplantiya_katil(self):
        print("toplantıya katıldı")

    def hesap_yap(self):
        print("hesap yap")
    
    def cizim_yap(self):
        print("çizim yazıldı")
    
class Doktor:
    def __init__(self, isim:str, boy:int, kilo:int):
        self.isim= isim
        self.boy = boy
        self.kilo = kilo

    def yuru(self, adim_sayisi:int):
        print(str(adim_sayisi) + "adım yürüdü")

    def uyu(self):
        print("uyudu")

    def ameliyat_yap(self):
        print("Ameliyat yapıldı")
    
    def tedavi_uygula(self):
        print("tedavi uygulandı")

class Hemsire:
    def __init__(self, isim:str, boy:int, kilo:int):
        self.isim= isim
        self.boy = boy
        self.kilo = kilo

    def yuru(self, adim_sayisi:int):
        print(str(adim_sayisi) + "adım yürüdü")

    def uyu(self):
        print("uyudu")

    def ameliyat_yap(self):
        print("Ameliyat yapıldı")

    def igne_yap(self):
        print("İğne yapıldı")

class UstaAsci:
    def __init__(self, isim:str, boy:int, kilo:int):
        self.isim= isim
        self.boy = boy
        self.kilo = kilo

    def yuru(self, adim_sayisi:int):
        print(str(adim_sayisi) + "adım yürüdü")

    def uyu(self):
        print("uyudu")

    def yemek_yap(self):
        print("Yemek yapıldı")

    def malzeme_listesi_hazirla(self):
        print("Malzeme listesi hazırlandı")

class Yamak:
    def __init__(self, isim:str, boy:int, kilo:int):
        self.isim= isim
        self.boy = boy
        self.kilo = kilo

    def yuru(self, adim_sayisi:int):
        print(str(adim_sayisi) + "adım yürüdü")

    def uyu(self):
        print("uyudu")

    def yemek_yap(self):
        print("Yemek yapıldı")

    def sogan_kes(self):
        print("Soğan kesildi")        

class Ogrenci:
    def __init__(self, isim:str, boy:int, kilo:int):
        self.isim= isim
        self.boy = boy
        self.kilo = kilo

    def yuru(self, adim_sayisi:int):
        print(str(adim_sayisi) + "adım yürüdü")

    def uyu(self):
        print("uyudu")

    def ders_calis(self):
        print("Ders çalışıldı")
        
## Buradan sonrası  kalıtım ile yazılmış versiyon

class Insan:
    def __init__(self, isim:str, boy:int, kilo:int):
        self.isim= isim
        self.boy = boy
        self.kilo = kilo

    def yuru(self, adim_sayisi:int):
        print(str(adim_sayisi) + "adım yürüdü")

    def uyu(self):
        print("uyudu")   

class Muhendis(Insan):
    def toplantiya_katil(self):
        print("toplantıya katıldı")

    def hesap_yap(self):
        print("hesap yap")

class Saglikci(Insan):
    def tedavi_uygula(self):
        print("tedavi uygulandı")

class Asci(Insan):
    def yemek_yap(self):
        print("Yemek yapıldı")

class Ogrenci(Insan):
    def ders_calis(self):
        print("Ders çalışıldı")

class BilgisayarMuhendisi(Muhendis):
    def kod_yaz(self):
        print("kod yazıldı")

class InsaatMuhendisi(Muhendis):
    def __init__(self, diploma_yili:int):
        self.diploma_verilis_yili = diploma_yili
    
    def diploma_yil_yazdir(self):
        print(self.diploma_verilis_yili)

    def cizim_yap(self):
        print("çizim yazıldı")

class Doktor(Saglikci):
    def ameliyat_yap(self):
        print("Ameliyat yapıldı")

class Hemsire(Saglikci):
    def igne_yap(self):
        print("İğne yapıldı")

class UstaAsci(Asci):
    def malzeme_listesi_hazirla(self):
        print("Malzeme listesi hazırlandı")

    def menu_hazirla(self):
        print("Menü_hazır")

class Yamak(Asci):
    def sogan_kes(self):
        print("Soğan kesildi")

doktor_murat = Doktor("Murat Çabuk", 1.90, 80)
doktor_murat.tedavi_yap()

insaat__muhendisi_cem = InsaatMuhendisi("Cem Can", 1.90, 75)
insaat__muhendisi_cem.cizim_yap()

yamak_ali = Yamak("ali",1.80,70)
yamak_ali.yemek_yap()

usta_mehmet = UstaAsci("Mehmet",1.75,85)
yamak_ali.yemek_yap()

insaat__muhendisi_osman = InsaatMuhendisi("Osman",1.76,76,2012)
