from arac_yonetimi import Arac
from musteri_yonetimi import Musteri
import fatura_yonetimi as f
import random


def secenekleri_sun():
    print("""liste almak için 1
             satış için 2
             satış iptal için 3
             çıkış için 4""")

def uygulama_baslat():
    while True:
        secenekleri_sun()
        secenek = input(":")
        
        if secenek == "1":
            f.satilan_araclarin_listesi_getir()
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
            sonuc = f.arac_sat(musteri, arac, fatura_tutari,fatura_no)
            if sonuc:
                pass
            else:
                pass


        elif secenek == "3":
            f.satilan_araclarin_listesi_getir()
            silinecek_arac_indeks_no = int(input("silinecek aracın indeks numarsını giriniz: "))
            f.satisi_iptal_et(silinecek_arac_indeks_no)


        elif secenek == "4":
            break
        else:
            print("lütfen doğru seçeneği giriniz")

if __name__ == "__main__":
    print(" Uygulamamıza hoşgeldiniz. v1.23 ")
    uygulama_baslat()
else:
    print("Bu uygulama modül olarak kullanılamaz.")