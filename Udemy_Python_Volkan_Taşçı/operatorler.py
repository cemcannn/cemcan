#Aritmetik Operatörler
# +   Toplama
# -   Çıkarma
# *   Çarpma
# /   Bölme
# **  Üssü
# //  Taban Bölme
# %   Mod Alma

x = 100

if x % 2 == 0:
    print("Çift sayıdır.")

#Karşılaştırma Operatörleri
# ==  Eşitse
# !=  Eşit Değilse
# >   Büyükse
# <   Küçükse
# >=  Büyük Eşitse
# <=  Küçük Eşitse

giris = input("10 ile 100 arasında sayı girin")

giris = int(giris)

if giris > 50:
    print("50'den büyükse")
elif giris < 50:
    print("50'den küçükse")
else:
    print("50'ye eşittir")

#Bool Operatörleri
#   and
#   or
#   not

x = int(input("Sayi gir"))
y = int(input("Sayi gir"))

if x > 5 and y % 2 == 0:
    print("doğru")

if x > 5 or y % 2 == 0:
    print("doğru")

if not bool(x):
    print("Boş")

#Değer Atama Operatörleri

# =   Eşittir İşlemi
# +=
# -=
# *=
# **=
# /=
# //=
# %=

x = 5
print("İlk Hal:", x)

x += 1
print("1 Eklenmiş Hali", x)

#Aitlik Operatörü

# in

x = "abcdefg"

if "a" in x:
    print("Mevcut")

parola_belirleme = input("Parola Belirleyiniz")

if "_" in parola_belirleme:
    print("_ Kullanınız.")
else:
    print("Parola Başarılı")

# Kimlik Operatörü

# is işleci
# id fonksiyonu

a = 5
b = 5

if a == b:
    print("Aynı")

if a is b:
    print("Aynı")

#İkisi de aynı sonucu verir, fakat ilki eşitliğe bakar, "is" isekimliğe bakar.
print(id(a))
print(id(b))
print(id(5))