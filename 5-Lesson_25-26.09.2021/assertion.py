giriş = input("Merhaba! Adın ne? ")
assert len(giriş) != 0 , "İsim bölümü boş."
print("Hoşgeldiniz.")

# Developerın kendini doğrulamasını sağlar.

# İş birimi kuralı: sonuç her zaman pozitif olacak. abs() fonksiyonu

while True:
    sayi1 = input("Sayı 1'i giriniz : ")
    sayi2 = input("Sayı 2'yi giriniz : ")    
    try:
        sayi1 = int(sayi1)
        sayi2 = int(sayi2)
        sonuc = sayi1+sayi2
        # sonuc = abs(sonuc) #Mutlak değer fonksiyonu
        assert sonuc>0, "Sonuç her zaman pozitif çıkmalı, abs() fonksiyonunu çalıştırmalısınız."
        
        print(sonuc)
    except ValueError:
        print("Lütfen metin girmeyiniz.")
    except AssertionError:
        print("Lütfen toplama sonucunu pozitif giriniz.")
    secenek=input("""devam için "e", çıkmak için "h"ye basınız.""")
    if secenek == "h":
        break

    # Assert kodu son kullanıcıda çalıştırırken hep optimize olarak çalıştırılmalı, bunu cmd de çalıştırırken python -o olarak çalıştırılmalı