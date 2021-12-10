import os

int_number=1_200_000 # karıştırmamak için bu şekilde bir yazım tarzı var.
float_number=1_200.000_100
print(float_number)

buyuk_float=1000000000000000000000000000000000000.0
print(buyuk_float)
buyuk_float_2= 1e+10
print(buyuk_float_2)

a=100
b=10
print(a+b)
print(a-b)
print(a*b)
print(b/a)

os.system ("cls")

print(100/3) # python tüm bölme işlemlerinş float olarak yapar.
print(type(100/3))

print(100//10) # Eğer sayıyı integer istersen çift bölme kullanacaksın.
print(type(100//10))
print(3//2) 

os.system ("cls")

#İşlem önceliği

print(1-(2*3+5))

#Üst alma
print(2**3) 

#Modülüs : bölüm işleminden kalanı hesaplama
print(100%3)

print(3.3333333333333333 + 1.111111111111111111) # Belli bir sayıdan sonra son rakamı bir arttırıyor neden; float fonksiyonu çok hassas değil. hassaslar için "decimal" kullanılır.

#Math kütüphanesi import etme

import math

print(math.ceil(3/2)) # 3ün 2ye bölünden kalanı integer olarak bir üste yuvarlamak istiyorsan "ceil" kullanacaksın.
print(math.floor(3/2.2)) # 3ün 2ye bölünden kalanı integer olarak bir alta yuvarlamak istiyorsan "floor" kullanacaksın.

#Decimal kütüphanesi
from decimal import Decimal as D # decilmal kütüpahnesinden Decimal çağırmak istiyorum ve bunu da "D" olarak kullanmak istiyorum.
print(D(3.3333333333333333) + D(1.111111111111111111))

#kesirli ifadeleri yüklemek için Fraction

from fractions import Fraction as Fra

print(Fra(130,200))


# Round bir rakamı yukarıya yakınsa yukarı, aşağıya yakınsa aşağı çekiyor.
print(round(10.51))

#Ayrıca virgülden sonra kaç rakam olacağını da ayarlayabiliyorsun.

a=(10/3)
print(round(a,2))
print(round(a,3))
#WORKSHOP

#requirements
# 1. kullanıcıdan 2 float istenecek. (tip : cast işlemi yapılmalı) 
# 2. 4 işlem yapılacak sonuçları yazdırılacak
# 3. İnteger bölme yapılacak. (tip: cast işlemi yapılacak)
# 4. Rakamları yukarıya yuvarlayarak bölme işlemi yapılacak ve sonuç ekrana yazdırılacak. (math modülü import edilecek)

os.system ("cls")

sayi_1 = input("Birinci sayıyı giriniz")
sayi_2 = input("İkinci sayıyı giriniz")
sayi_1 = float(sayi_1)
sayi_2 = float(sayi_2)
print("Toplama {}".format(sayi_1+sayi_2))
print("Çıkarma {}".format(sayi_1-sayi_2))
print("Çarpma {}".format(sayi_1*sayi_2))
print("Bölme {}".format(sayi_1/sayi_2))
print("İnt Bölme {}".format(int(sayi_1/sayi_2)))
sayi_1 = math.ceil(sayi_1)
sayi_2 = math.ceil(sayi_2)
print("Bölme {}".format(sayi_1/sayi_2))