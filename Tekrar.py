#1. ders

# cem = "sana gül bahçesi vaadettim."
# cem1 = cem.upper()
# print(cem1)

# cem = cem1.lower()
# print(cem)

# cemo = "1,2,3,4"
# cemo1 = cemo.split("+")
# print(cemo1)

# cema = "hojgeldin"
# cema1 = cema.replace("j","ş")
# print(cema1)

# buyuk_metin = "merhaba nasılsın? \n iyiyim"
# splitlines_metin = buyuk_metin.splitlines()
# print(splitlines_metin)

# halo = "          mata     "
# halo = halo.strip()
# print(halo)
# halo = halo.capitalize()
# print(halo)

# halo = "HALOOOO"
# print(bool(halo.isupper()))

# kelo = "1"
# print(bool(kelo.isnumeric()))

# melo = "klşrhlkancvfasjdlkjfh832u4y2384u"
# print(melo.find("a"))
# print(melo.find("b"))
# print(melo.index("a"))
# print(melo.index("b"))
# print(melo.count("a"))
# print(len(melo))

#2. ders

# sayi = 1e+10
# print(sayi)

# import math
# print(math.ceil(3/2))
# print(math.floor(3/2))

# from decimal import Decimal as D
# print(D(1.113151661561616)+D(2.651651884168106))    

# from fractions import Fraction as F
# print(F(130,200))
# print(F(135,176))

# a = 13.246
# print(round(a,2))

# b=13.5
# print(round(b))

# 3. Ders

# liste = [1,2,3,4,"dssd","1",12.4,[7,8,["cem",5]]]

# print(liste[7][2][0])
# print(liste[-1])
# print(liste[::-1])
# liste.append("maymun")
# print(liste)
# liste.append([1,2,3])
# liste.append([[1,2,3]])
# liste.extend([1,2,3])
# print(liste)

# liste5=[1,2,3]
# del liste5[0]
# print(liste5)

# liste.remove(2)
# print(liste)

# liste.append(2)
# print(liste)

# liste.pop(2)
# print(liste)

# print(liste.count(2))

# kume1 = {1,2,3,4}
# kume2 = {(1,2,3),7,5,5,4,"a","b"}
# print(kume2)

# print(len(kume2))

# kesisim_kumesi = kume1.intersection(kume2)
# print(kesisim_kumesi)

# fark_kumesi = kume2.difference(kume1)
# print(fark_kumesi)

# kume_sim_fark = kume2.symmetric_difference(kume1)
# print(kume_sim_fark)

# kume1.pop()

# tuple1=(1,2,4,5,3,"elma",[1,"2"],"a",True)
# print(tuple1)

# print(len(tuple1))
# print(tuple1.count(1))
# liste = tuple1[6]

# tuple2=(1,5,3,5,8,2)
# print(sorted(tuple2))
# print(tuple2)

# sozluk = {1:"elma",2:"Armut",3:"Kiraz",4:"Dört"}
# print(sozluk)
# print(sozluk[1])

# sozluk5 = dict([(1,"bir"),("beş",5)])
# print(sozluk5)

# print(sozluk.get(2))
# print(sozluk.get("elma"))

# print(sozluk.keys())
# print(sozluk.values())
# print(sozluk.items())

# sozluk[1]="bir"
# print(sozluk)

# metin = input("bir şeyler girin")

# if metin.isnumeric() == True:
#     if int(metin)>100:
#         print("sayı 100'den büyük")
#     else:
#         print
#     print("sayı 100'den küçük veya 100'e eşit")
# elif metin.isnumeric() != True:
#     print("Sayı girmediniz.")

# else:
#     print("Abuu")

# Kullanıcıdan iki rakam alınacak, rakam olduğuna emin olun.
# Kullanıcıya yapmak istediği işlem için seçenek sunulacak
#     -Seçenekler
#         - Toplama
#         - Çıkartma
#         - Çarpma
# - Kullanıcı hangisini seçerse işlem yapılıp ekrana yazdırılacak (seçenek kontrolü)


rakam1 = input("Rakam 1'i giriniz : ")
rakam2 = input("Rakam 2'yi giriniz : ")

durum=False

while durum==False:
    if (rakam1.isnumeric() and rakam2.isnumeric()) == True:
        secenek = input(""" 
                            Toplama = (+)
                            Çıkarma = (-)
                            Çarpma  = (*)
                            Bölme   = (/)

        Lütfen yapmak istediğiniz işlemi giriniz : """)
        if secenek == "+":
            print(int(rakam1) + int(rakam2))
            durum==True
        elif  secenek == "-":
            print(abs(int(rakam1)-int(rakam2)))
            durum==True
        elif secenek == "*":
            print(int(rakam1)*int(rakam2))
            durum==True
        elif secenek == "/":
            try:
                print(int(rakam1)/int(rakam2))
                durum=1
            except ZeroDivisionError:
                print("""Bölen "0" olamaz!""")
                continue
        else:
            print("Lütfen rakam giriniz!")
            continue


