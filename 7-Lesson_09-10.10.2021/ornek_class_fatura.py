faturalar=[]
import random

class Musteri: # Müşteri class ını tanımlıyoruz.
    def __init__(self): # Class ilk tanımlamalarda her zaman init başlar, self yerine başka bir tanımlama da gelebilir fakat burada self o class ın içinde başka bir tanımlama yapmamızı sağlıyor, mesela insan class ının içinde cem veya ahmet gibi.
        self.adi="" # Müşteri adı self ile tanımlanıyor, burada her bir müşteri self olarak gelecek.
        self.tckn="" 
        self.tel=""

class Arac:
    def __init__(self): 
        self.marka = ""
        self.model = ""
        self.renk= ""
        self.maksimum_hiz=0
        self.id = ""
        self.yaptigi_km = 0
    
    def calistir(self):
        print(f"{self.id} seri numaralı araç çalıştı")
    
    def durdur(self):
        print(f"{self.id} seri numaralı araç durduruldu")
    
    def git(self, km:int):
        print(f"{self.id} seri numaralı araç hareket etti")
        self.yaptigi_km = self.yaptigi_km + km
    def gittigi_km_sayacini_yazdir(self):
        print(str(self.yaptigi_km))

class Fatura:
    def __init__(self): 
        self.arac = ""
        self.musteri = ""
        self.tutar = 0
        self.fatura_no=0
# Aşağıda araç sat fonksiyonu ile müşteri parametresinin Müşteri class ına eşit olduğunu, diğer parametrelerin de diğer fonksiyonları çağırdığını ve çıkışın da bool olarak (True or False) çıktığını ifade eder.
def arac_sat(musteri_parametresi:Musteri, arac_parametresi:Arac, tutar_parametresi:int) -> bool: 
    fatura = Fatura()
    fatura.arac = arac_parametresi
    fatura.musteri = musteri_parametresi
    fatura.tutar = tutar_parametresi
    fatura.fatura_no = random.randint(1000, 10000) # Fatura numarası random olarak geliyor.

    try:
        faturalar.append(fatura) 
    
    except Exception as ex:
        print(ex.message)
        print("Araç Satılamadı")
        return False
    else:
        print("Araç Satıldı")
        return True

def satilan_araclarin_listesi_getir(): 
    template = "Indeks: {}, Fatura No: {}, TCKN: {}, Ad: {}, Seri No: {}, Marka/Model: {}/{}, Tutar:{}"
    indeks=0
    for fatura in faturalar:
        print(template.format(indeks,fatura.fatura_no, fatura.musteri.tckn,fatura.musteri.adi,
                                fatura.arac.id, fatura.arac.marka,fatura.arac.model,fatura.tutar ))
        indeks = indeks + 1
        print("-----------------------------------------------------------------------------------")

def satisi_iptal_et(fatura_indeks:int):
    silinecek_fatura = faturalar[fatura_indeks]
    print("Silinecek fatura no : " + str(silinecek_fatura.fatura_no))
    secenek = input("fatura silinecek emin misiniz? silek için e, iptaletmek  için h")
    if secenek == "e":
        faturalar.pop(fatura_indeks)
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
        
        sonuc = arac_sat(musteri, arac, fatura_tutari)
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




