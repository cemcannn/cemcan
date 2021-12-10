
class Ogretmen:
    def __init__(self):
        self.adi            = ""
        self.soyadi         = ""
        self.girdigi_ders   = ""

class Ders:
    def __init__(self):
        self.adi            = ""
        self.no             = ""
        self.kredisi        = ""

class Ders_kaydi:
    alinan_dersler          =[]
    def __init__(self,ogretmen:Ogretmen,ders_adi:Ders,ders_no:int,ders_kredisi:int):
        self.ogretmen       = ogretmen
        self.ders_adi       = ders_adi
        self.ders_no        = ders_no
        self.ders_kredisi   = ders_kredisi
        self.alinan_dersler.append(self)
  
    def ogrenci_cagir(self):
        return self.ogrenci.adi

    def ogretmen_cagir(self):
        return self.ogretmen.adi

    @classmethod
    def tum_dersleri_getir(cls):
        return cls.alinan_dersler

    @classmethod
    def dersi_sil(cls, ders_indeks_no:int):
        cls.alinan_dersler.pop(ders_indeks_no)

    @classmethod
    def ders_getir(cls, ders_indeks_no:int):
        return cls.alinan_dersler[ders_indeks_no]

def ders_kaydet(ogretmen:Ogretmen,ders_adi:Ders,ders_no:int,ders_kredisi:int):
    ders = Ders_kaydi(ogretmen,ders_adi,ders_no,ders_kredisi)
    print("Ders kaydı yapıldı.")

def listeyi_getir():
    template = "Indeks: {}, Öğretmen Adı: {}, Öğretmen Soyadı: {}, Ders Adı: {}, Ders No: {},Ders Kredisi: {}"
    indeks=0

    for dersler in Ders_kaydi.tum_dersleri_getir():
        print(template.format(indeks,dersler.ogretmen.adi,dersler.ogretmen.soyadi, dersler.ders_adi.adi,dersler.ders_no,
                                dersler.ders_kredisi))
        indeks = indeks + 1

def ders_iptal_et(ders_indeks:int):
    cikarilacak_ders = Ders_kaydi.ders_getir(ders_indeks)
    print("Cikarilacak ders no : " + str(cikarilacak_ders.ders_adi.adi))
    secenek = input("ders cikarilacak emin misiniz? çıkarmak için (e), iptal etmek  için (h) :")
    if secenek == "e":
        Ders_kaydi.dersi_sil(ders_indeks)
        print("Ders kaydı silindi")

def secenekleri_sun():
    print("""
            Tüm dersleri görmek için           (1)
            Derse kaydolmak için               (2)
            Dersi çıkarmak için                (3)
            Dönem ders kayıt işlemini tamamla  (4)
            Çıkış için                         (5)
             """)

while True:
    secenekleri_sun()
    secenek = input("")
    
    if secenek == "1":
        listeyi_getir()
    elif secenek == "2":
        ders_adi = Ders()
        ders_adi.adi = input("Ders adını giriniz : ")
        ders_adi.ders_no = input("Ders numarası giriniz : ")
        ders_adi.ders_kredisi = input("Ders kredisi giriniz : ")
        
        ogretmen        = Ogretmen()
        ogretmen.adi    = input("Öğretmen adını giriniz : ")
        ogretmen.soyadi = input("Öğretmen soyadını giriniz : ")
        ogretmen.girdigi_ders = ders_adi

        sonuc = ders_kaydet(ogretmen, ders_adi, ders_adi.ders_no, ders_adi.ders_kredisi)
        if sonuc:
            pass
        else:
            pass

    elif secenek == "3":
        listeyi_getir()
        cikarilacak_ders_indeks_no = int(input("çıkarılacak dersin indeks numarsını giriniz: "))
        ders_iptal_et(cikarilacak_ders_indeks_no)

    elif secenek == "4":
        print("Kayıt işlemi başarıyla tamamlandı.")
        break
    
    elif secenek == "5":
        break

    else:
        print("lütfen doğru seçeneği giriniz")




