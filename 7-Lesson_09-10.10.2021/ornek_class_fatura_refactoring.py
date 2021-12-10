
import random

class Musteri:
    def __init__(self):
        self.adi    = ""
        self.tckn   = ""
        self.tel    = ""

class Arac:
    def __init__(self):
        self.marka  = ""
        self.model  = ""
        self.renk   = ""
        self.hiz    = 0
        self.id     = ""
        self.km     = 0
    
    def calistir(self):
        print(f"{self.id} seri numaralı araç çalıştı")
    
    def durdur(self):
        print(f"{self.id} seri numaralı araç durduruldu")
    
    def git(self, km:int):
        print(f"{self.id} seri numaralı araç hareket etti")
        self.km = self.km + km
    def gittigi_km_sayacini_yazdir(self):
        print(str(self.km))

class Fatura:
    faturalar=[]
    def __init__(self,arac:Arac,musteri:Musteri,tutar:int,fatura_no:int):
        self.arac       = arac
        self.musteri    = musteri
        self.tutar      = tutar
        self.fatura_no  = fatura_no
        self.faturalar.append(self)
    
    def fatura_musteri_getir(self):
        return self.musteri.adi
    
    @classmethod
    def tum_faturalari_getir(cls):
        return cls.faturalar
    
    @classmethod
    def faturayi_faturalardan_sil(cls, fatura_indeks_no:int):
        cls.faturalar.pop(fatura_indeks_no)
        
    @classmethod
    def fatura_getir(cls, fatura_indeks_no:int):
        return cls.faturalar[fatura_indeks_no]

def arac_sat(musteri_parametresi:Musteri, arac_parametresi:Arac, tutar_parametresi:int, fatura_no_parametresi:int):
    fatura = Fatura(arac_parametresi,musteri_parametresi,tutar_parametresi,fatura_no_parametresi)
    print("Araç Satıldı")
 
def satilan_araclarin_listesi_getir():
    template = "Indeks: {}, Fatura No: {}, TCKN: {}, Ad: {}, Seri No: {}, Marka/Model: {}/{}, Tutar:{}"
    indeks=0

    for fatura in Fatura.tum_faturalari_getir():
        print(template.format(indeks,fatura.fatura_no, fatura.musteri.tckn,fatura.musteri.adi,
                                fatura.arac.id, fatura.arac.marka,fatura.arac.model,fatura.tutar ))
        indeks = indeks + 1
        print("-----------------------------------------------------------------------------------")

def satisi_iptal_et(fatura_indeks:int):
    silinecek_fatura = Fatura.fatura_getir(fatura_indeks)
    print("Silinecek fatura no : " + str(silinecek_fatura.fatura_no))
    secenek = input("fatura silinecek emin misiniz? silek için e, iptaletmek  için h")
    if secenek == "e":
        Fatura.faturayi_faturalardan_sil(fatura_indeks)
        print("fatura silindi")

def secenekleri_sun():
    print("""liste almak için 1
             satış için 2
             satış iptal için 3
             çıkış için 4""")

while True:
    secenekleri_sun()
    secenek = input(":")
    
    if secenek == "1":
        satilan_araclarin_listesi_getir()
    elif secenek == "2":
        arac = Arac()
        arac.id=input("aracın id sini giriniz")
        arac.marka = "Ford"
        arac.model="Focus"
        
        musteri = Musteri()
        musteri.tckn=input("kişi tckn giriniz: ")
        musteri.adi = "Murat Çabuk"
        musteri.tel = "34534453"
        fatura_tutari = int(input("tutar giriniz: "))
        

        fatura_no = random.randint(1000, 90000)
        sonuc = arac_sat(musteri, arac, fatura_tutari,fatura_no)
        if sonuc:
            pass
        else:
            pass


    elif secenek == "3":
        satilan_araclarin_listesi_getir()
        silinecek_arac_indeks_no = int(input("silinecek aracın indeks numarsını giriniz: "))
        satisi_iptal_et(silinecek_arac_indeks_no)


    elif secenek == "4":
        break
    else:
        print("lütfen doğru seçeneği giriniz")





