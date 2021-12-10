import Ogrenci
import Ders 

class Donem_kaydi:
    alinan_dersler          =[]
    def __init__(self,ogrenci:Ogrenci,ders_adi:Ders):
        self.ogrenci        = ogrenci
        self.ders_adi       = ders_adi
        self.alinan_dersler.append(self)

    @classmethod
    def dersleri_listele(cls):
        return cls.alinan_dersler

    @classmethod
    def ders_sil(cls, ders_indeks_no:int):
        cls.alinan_dersler.pop(ders_indeks_no)

    @classmethod
    def ders_getir(cls, ders_indeks_no:int):
        return cls.alinan_dersler[ders_indeks_no]

def ogrenci_kaydet(ogrenci:Ogrenci, ders_adi:Ders):
    kayit = Donem_kaydi(ogrenci,ders_adi)
    print("Ders kaydı yapıldı.")
 
def ders_listesini_getir():
    template = "index : {}, Ders no: {}, Öğrenci adı: {}, Öğrenci soyadı: {}, Ders adı: {}, Ders kredisi : {}"
    indeks = 0

    for dersler in Donem_kaydi.dersleri_listele():
        print(template.format(indeks,Ders.no, Ogrenci.adi,Ogrenci.soyadi, Ders.adi, Ders.kredisi))
        indeks = indeks + 1
        print("-----------------------------------------------------------------------------------")

def ders_sil(ders_indeks:int):
    silinecek_ders = Donem_kaydi.ders_getir(ders_indeks)
    print("Silinecek ders adı : " + str(silinecek_ders.ders_adi))
    secenek = input("Ders silinecek emin misiniz? silmek için e, iptal etmek  için h")
    if secenek == "e":
        Donem_kaydi.ders_sil(ders_indeks)
        print("Ders silindi")
