import Ders
import Ogrenci
import Donem_kaydi as dk

def secenekleri_sun():
    print("""
    Lütfen bir seçenek seçiniz:
    (1) Dersleri listeleme
    (2) Ders kaydı
    (3) Dersleri sil
""")

def uygulama_baslat():
    while True:
        secenekleri_sun()
        secenek = input(":")
        
        if secenek == "1":
            dk.ders_listesini_getir()
        elif secenek == "2":
            ogrenci = Ogrenci
            ogrenci.adi=input("öğrenci adı giriniz")
            ogrenci.soyadi =input("öğrenci soyadı giriniz")
            ogrenci.numarasi=input("öğrenci numarası giriniz")
            
            ders = Ders
            ders.adi=input("ders adı giriniz")
            ders.no = input("ders numarası giriniz")
            ders.kredisi = input("ders kredisi giriniz")

            dk.ogrenci_kaydet(ogrenci,ders)

        elif secenek == "3":
            dk.ders_listesini_getir()
            silinecek_ders_indeks_no = int(input("silinecek dersin indeks numarsını giriniz: "))
            dk.ders_sil(silinecek_ders_indeks_no)

        elif secenek == "4":
            break
        
        else:
            print("lütfen doğru seçeneği giriniz")

if __name__ == "__main__":
    print(" Uygulamamıza hoşgeldiniz. v1.23 ")
    uygulama_baslat()
else:
    print("Bu uygulama modül olarak kullanılamaz.")