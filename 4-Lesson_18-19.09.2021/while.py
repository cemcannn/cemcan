import os

deger=True

# while deger==True:
#     print("True") #Sürekli ekrana True yazdırır, eğer durdurmak isteersen "Ctrl + C"
# sayi=15


os.system ("cls")

sayi = 5

while sayi > 0:
    print(f"Sayı halen sıfırdan büyük: {sayi}")
    sayi = sayi - 1


liste = [1,2,3,4,5,6]
sayi2 = len(liste) - 1

while sayi2 >= 0:
    print(f"deger: {liste[sayi2]}")
    sayi2 = sayi2 - 1

personel_adi = "murat"

personel_listesi = ["murat", "selim", "murat", "murat", "ahmet", "oğuz", "ali"]
while personel_adi in personel_listesi:   # Bir listede check edilmesi gereken bir isim varsa onu check eder
    print(f"personel adi : {personel_adi}")
    personel_listesi.remove("murat")

os.system ("cls")

i=0
t=0
while 1==1:
    i = i + 1
    deger = input("10'dan büyük bir sayı giriniz:")

    while deger.isnumeric() == False:
        deger = input("Lütfen rakam giriniz:")
        continue

    rakam = int(deger)

    if rakam < 11:
        print("yanlış karar 10'dan büyük bir sayı girmediniz.")
    else:
        print(rakam + 5)
    
    secenek = input("""
                        devam etmek için    (e) 
                        çıkmak için         (h) 
                        yazıp enter tuşuna basınız : """)
    
    if secenek == "e":
        t = t + 1
        print(f"program {i} kez çalıştı, {t} kez devam edildi.")
        pass
    elif secenek == "h":
        print("programdan başarıyla çıktınız.")
        break
    else:
        print("lütfen doğru seçeneği giriniz.")

os.system ("cls")


