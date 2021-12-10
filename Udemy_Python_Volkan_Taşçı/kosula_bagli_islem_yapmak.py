x = int(input("Bir rakam giriniz"))

if x == 5:
    print("Doğru rakamı girdiniz.")
else:
    print("Tekrar deneyiniz.")

y = input("Bir şey giriniz")

if bool(y):                 #bu şekilde boş değer verirsek y ye bool false çıkar.
    print("İçerisi dolu")
else:
    print("İçerisi boş")

#Hesap makinesi orta seviye

a = int(input("Birinci sayıyı giriniz : "))
b = int(input("İkinci sayıyı giriniz : "))

print("""  

[1] Toplama İşlemi
[2] Çıkarma İşlemi
[3] Çarpma İşlemi
[4] Bölme İşlemi
[5] Üs Alma İşlemi
[Q] Çıkış

        """) #3 adet kesme işaretinde istediğin gibi parantez içini düzenleyebilirsin.

giris = input("Seçiminiz : ")

if giris == "1":
    print("Toplama işlemi Sonucu : ", a + b )

elif giris == "2":
    if a <= b:
        print("Çıkarma İşlemi Sonucu : ", b - a)
    else:
        print("Çıkarma İşlemi Sonucu : ", a - b)

elif giris == "3":
    print("Çarpma işlemi Sonucu : ", a * b )

elif giris == "4":
    if a <= b:
        print("Bölme İşlemi Sonucu : ", b / a)
    else:
        print("Bölme İşlemi Sonucu : ", a / b)

elif giris == "5":
    print(f"{a} üzeri {b} : ", a ** b ) 

elif giris == "Q" or "q":
    print("Çıkış Yapılıyor.")

else:
    print("Yanlış Giriş Yaptınız Tekrar Deneyiniz.")