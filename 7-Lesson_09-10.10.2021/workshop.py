# öğretmen, öğrenci ve donem derslerine kayıt kurgusunu daha once 
# yaptımız araç,müsteri ve fatura kurgusundaki örneğe enzer şekiklde yapınız
# Tip: ogretmen,ogrenci ile donem_dersi_kaydi örneklerinizi 
# donem_ders_kayitlari(donem_dersi_kaydi objeslerinden oluşan) listede birleştriniz. 

class Ogretmen:
    def __init__(self,ad,tckn):
        self.ad = ad
        self.tckn=tckn

class Ogrenci:
    def __init__(self,ad,tckn):
        self.ad = ad
        self.tckn=tckn


class Ders:
    def __init__(self,ders_adi, ders_kodu):
        self.ders_adi = ders_adi
        self.ders_kodu=ders_kodu

class DersDonem:
    def __init__(self,yil, donem):
        self.yil = yil
        self.donem=donem


class DonemDersiKaydi:
    donem_dersi_kayitlari = []
    def __init__(self,ogrenci,ogretmen,ders,ders_donem):
        self.ogrenci = ogrenci
        self.ogretmen = ogretmen
        self.ders = ders
        self.donem = ders_donem
        self.donem_dersi_kayitlari.append(self)

    @classmethod
    def donem_ders_kayitlarini_getir(cls):
        return cls.donem_dersi_kayitlari

    @classmethod
    def donem_ders_kaydi_sil(cls, donem_ders_kaydi_indeks_no) -> bool:
        cls.donem_dersi_kayitlari.pop(donem_ders_kaydi_indeks_no)
        return True




def secenekleri_sun():
    print("""
            liste almak için 1
            dersi kaydı için 2
            ders kaydi silmek için için 3
            çıkış için 4""")


while True:
    secenekleri_sun()
    secenek = input(": ")
    
    if secenek == "1":
        donem_ders_kayitlari = DonemDersiKaydi.donem_ders_kayitlarini_getir()
        for donem_ders_kaydi in donem_ders_kayitlari:
            print(donem_ders_kaydi.ders.ders_adi, donem_ders_kaydi.ogretmen.ad, donem_ders_kaydi.ogrenci.ad)

    elif secenek == "2":

        ogrenci= Ogrenci(input("ad giriniz:"),input("tckn giriniz:"))
        ogretmen= Ogretmen(input("ad giriniz:"),input("tckn giriniz:"))
        ders= Ders(input("ders adı giriniz:"),input("ders kodu giriniz:"))
        ders_donemi= DersDonem(input("yıl giriniz:"),input("donem giriniz:"))

        donem_ders_kaydi = DonemDersiKaydi(ogrenci,ogretmen,ders,ders_donemi)
        


    elif secenek == "3":
        print(DonemDersiKaydi.donem_ders_kayitlarini_getir())
        silinecek_ders_kayit_indeks_no = int(input("silinecek ders kayit indeks numarsını giriniz: "))
        DonemDersiKaydi.donem_ders_kaydi_sil(silinecek_ders_kayit_indeks_no)


    elif secenek == "4":
        break
    else:
        print("lütfen doğru seçeneği giriniz")



