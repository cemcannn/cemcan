## True False
## Bool - Boolean


### logical operator
# mantıksal operatorler


# a = True
# print(a)

# if 1 == 1:
#     print("1 1 e eşit")

# if 1 < 2:
#     print("1 2 den küçük")

# if 1 > 0: # eğer 1 0 dan büyükse
#     print("1 0 dan büyük") # ekrana bu metni yaz

# sayi1 = input("bir sayi giriniz")

# sayi1=int(sayi1)

# if sayi1 >= 1:
#     print("girdiğiniz sayi 1 eşit veya 1 den büyük")

# if sayi1 > 1 and sayi1 < 5:
#     print("girdiğiniz sayı 1 den büyük 5 den küçük") 


# if sayi1 > 1 or sayi1 < 5:
#     print("girdiğiniz sayı 1 den veya 5 den küçük")


# if (True or False) and (True and True):
#     print("Herşey doğru")

# sayi2 = int(input("sayi giriniz: "))
# if (sayi2 > 100 or sayi2 <= 500) and sayi2==300:
#     print ("sayi 300 e eşit")


# if sayi2%2==0 and sayi2 > 100:
#     print("girdiğiniz sayı 100 den büyük çift sayıdır")

# sayi3 = input("birşeyler giriniz: ")

# if sayi3.isnumeric():
#     print("girdiğiniz değer sayıdır")

# if sayi3.isnumeric()==False:
#     print("girdiğiniz değer sayı değildir")

# # üstteki 2 satırın farklı yazımı

# if sayi3.isnumeric():
#     print("girdiğiniz değer sayıdır")
# else:
#     print("ne girdiğinizi anlamadım")

# # elif

# metin = input("tek kelime giriniz: ")

# if metin == "merhaba":
#     print ("merhaba murat")
# elif metin == "selam":
#     print("selam selim")
# elif metin == "ola":
#     print("ola khoze")
# else:
#     pass


# # not kullanımı
# liste = [1,2,3]

# if not type(liste) == str:
#     print("değişkenin tipi string değildir dir")

metin = input("birşeyler girin: ")

if metin.isnumeric(metin) == True:
    if int(metin) > 100:
        print("sayı 100 den büyük")
    else:
        print("sayı 100 den küçük veya 100 e eşit")

else:
    if metin == "merhaba":
        print("merhaba murat")
    elif metin == "selam":
        print("merhaba selim")
    else:
        pass



# üstteki kod alttaki gibi yazılabilirdi


metin = input("birşeyler girin: ")

if metin.isnumeric(metin) and int(metin) > 100:
    print("sayı 100 den küçük veya 100 e eşit")

else:
    if metin == "merhaba":
        print("merhaba murat")
    elif metin == "selam":
        print("merhaba selim")
    else:
        pass

a = 10

if a > 50 and a < 100:
    print ("")






























    







