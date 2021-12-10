# Kullanıcıdan iki rakam alınacak, rakam olduğuna emin olun.
# Kullanıcıya yapmak istediği işlem için seçenek sunulacak
#     -Seçenekler
#         - Toplama
#         - Çıkartma
#         - Çarpma
# - Kullanıcı hangisini seçerse işlem yapılıp ekrana yazdırılacak (seçenek kontrolü)

Rakam1 = input("Birinci rakamı giriniz : ")
Rakam2 = input("İkinci rakamı giriniz : ")

if Rakam1.isnumeric():
    Rakam1=int(Rakam1)
else:
    print("Rakam giriniz")

if Rakam2.isnumeric():
    Rakam2=int(Rakam2)
else:
    print("Rakam giriniz")

Islem = input("İşlem seçiniz\n - Toplama\n - Çıkarma\n - Çarpma\n Yapmak istediğiniz işlemi yazınız: ")

if type(Rakam1) and type(Rakam2) == int:
    if Islem == "Toplama":
        print(Rakam1+Rakam2)
    elif Islem=="Çıkarma":
        print(Rakam1-Rakam2)
    elif Islem=="Çarpma":
        print(Rakam1*Rakam2)
    else:
        print("Lütfen doğru işlemi seçiniz!")
else:
    pass