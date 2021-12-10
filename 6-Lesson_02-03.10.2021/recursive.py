# Recursive function kendi kendini yenileyen fonksiyondur.

# def ekranayaz():
#     print("merhaba")
#     ekranayaz()

# from sys import getrecursionlimit, setrecursionlimit
# print(getrecursionlimit())
# setrecursionlimit(10000)
# print(getrecursionlimit())

# def geri_sayim(sayi):
#     print(sayi)
#     if sayi==0:
#         return
#     else:
#         sayi -= 1
#     geri_sayim(sayi)

# geri_sayim(3)

# Eğer yukarıdaki örnekte 1 sayısını yazdırmak istemiyorsan.

# def geri_sayim(sayi):
#     if sayi!=1:
#         print(sayi)
#     if sayi==0:
#         return
#     else:
#         sayi -= 1
#     geri_sayim(sayi)

# geri_sayim(3)

# Yukarıdaki örneği for ile yapmak.

# def geri_sayim(sayi):
#     for i in list(range(0,sayi))[::-1]:
#         print(i)

# geri_sayim(3)

# def geri_sayim(sayi):
#     for i in list(reversed(range(0,sayi))):
#         print(i)

# geri_sayim(3)

#Nested listelerde kullanım

# liste = ["Ahmet",["Mehmet", 1,2],[1,2,3,["Murat","Atıf",["Selim","Tuğçe","Görkem",[1,2,3,4]]]]] #Bu listenin içinde dolanmak için.

# def listeyi_ekrana_yaz(liste_parametresi):
#     for liste_elemani in liste_parametresi:
#         if type(liste_elemani)!= list:
#             print(liste_elemani)
#         else:
#             listeyi_ekrana_yaz(liste_elemani)

# listeyi_ekrana_yaz(liste)

# Faktöriyel hesabı



