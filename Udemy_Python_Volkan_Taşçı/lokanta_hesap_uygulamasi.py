
masalar = dict()
for i in range(10):
    masalar[i]=0

def hesap_ekle():
    masa_no = int(input("Lütfen masa numarası giriniz : "))
    gecerli = masalar[masa_no]
    eklenecek = float(input("Lütfen eklenecek hesap miktarını giriniz : "))
    toplam = gecerli + eklenecek
    masalar[masa_no] = toplam

def hesap_sil():
    masa_no = int(input("Lütfen masa numarası giriniz : "))
    gecerli = masalar[masa_no]
    eksilecek = float(input("Lütfen düşülecek hesap miktarını giriniz : "))
    toplam = gecerli + eksilecek
    if toplam < 0:
        print("İşlemde hata var, lütfen kontrol ediniz!")
    else:
        masalar[masa_no] = toplam

def hesap_kontrol(dosya_adi):
    try:
        dosya=open(dosya_adi)
        veriler = dosya.read()
        veriler=veriler.split("\n")
        veriler.pop()
        dosya.close()
        flag = True
    
    except FileNotFoundError:
        dosya=open(dosya_adi,"w")
        dosya.close()
        print("İlk kez çalıştırıldı, kayıt dosyası yaratıldı...")
        flag = False

    if flag:
        for i in enumerate(veriler):
            masalar[i[0]]=float(i[1])
    else:
        pass

def kayit_guncelle():
    dosya= open("kayıtlar.txt","w")
    for i in range(10):
        ucret = masalar[i]
        ucret = str(ucret)
        dosya.write(ucret + "\n")
    dosya.close()

def main():
    hesap_kontrol("kayıtlar.txt")
    kayit_guncelle()
    while True:
        print("""
        [1] Masaları Görüntüle
        [2] Hesap Ekle
        [3] Hesap Sil
        [4] Çıkış    
        """)

        secim = input("İşleminizi Seçiniz : ")
        
        if secim == "1":
            for i in range(10):
                print(f"Masa Numarası : {i}, Hesap Miktarı {masalar[i]}")

        elif secim == "2":
            hesap_ekle()
            kayit_guncelle()

        elif secim == "3":
            hesap_ekle()
            kayit_guncelle()
            
        elif secim == "4":
            print("Çıkış yapılıyor...")
            quit()

        else:
            print("Lütfen geçerli bir seçim yapınız!")

main()