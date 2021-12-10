from arac_yonetimi import Arac
from musteri_yonetimi import Musteri

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

