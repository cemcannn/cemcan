
# def gunaydin_yaz():
#     print("günaydın")

# gunaydin_yaz()

# #Python overload desteklemiyor.
# def gunaydin_yaz(isim): #Method overriding yaptık yani üstteki metodu ezdik.
#     print(isim + " Günaydın")

# gunaydin_yaz("Cem")

# isim = "Cem"
# ad = "Mehmet"
# def merhaba_de():
#     isim = "Ahmet"
#     print("Merhaba ", isim)

#     ad = "Osman"
#     print("Merhaba ", ad)
#     sayi = 2
#     print(locals()) #Local alan içerisinde bütün verileri getirir. 
#     print(globals()) #Fonksiyon içinde dahi global alanı gösterir.

# merhaba_de()
# print(isim)
# print(globals()) #Global alan verilerini gösterir.
# print(locals()) # Fonksiyon dışında olduğuiçin global verileri getirir.

# # Global alandaki bir değişkene fonksiyondan bir değer atamak için global keyword kullanılır.

# a = 2

# def ekrana_yaz(sayi): #Global alandaki ekrana yazılan bir değeri değiştirmek için.
#     global a
#     a = 2 + sayi
#     print(locals())

# ekrana_yaz(3)
# print(a) # "a" değişiyor.

## Değer föndürmek

# def hesapla(sayi):
#     a = (sayi * 2) / 2 + (sayi - 2)
#     if a%2 == 1:
#         sayi2 = input("sayi 2 giriniz : ")
#     else:
#         sayi2 = 2
#     return a * int(sayi2)
    
# sonuc = hesapla(4)
# print(sonuc)

# Birden fazla değer döndürmek

# def dort_islem_hesapla():
#     sayi1 = int(input("sayi1 : "))
#     sayi2 = int(input("sayi2 : "))

#     toplama_sonucu = sayi1 + sayi2
#     cikarma_sonucu = sayi1 - sayi2
#     bolme_sonucu = sayi1 / sayi2
#     carpma_sonucu = sayi1 * sayi2

#     return toplama_sonucu, cikarma_sonucu,\
#             bolme_sonucu, carpma_sonucu

# print(dort_islem_hesapla())

# my_tuple = dort_islem_hesapla() 
# a = my_tuple[0]
# b = my_tuple[1]
# c = my_tuple[2]
# d = my_tuple[3]
# print(a)

# #Ya da şöyle olabilir.

# e,f,g,h = dort_islem_hesapla() # Direkt değeri atıyoruz.
# print(e)

# # Birden fazla return kullanmak.

# def deger_dondur(sayi):
#     if sayi == 10:
#         return "sayı 10"
#     elif sayi == 20:
#         return "sayı 20"
#     else:
#         return "diğerleri"

# # Limitli sonsuz döngü

# def basla():   
#         print("Başla fonksiyonu çalıştı.")
#         devam_et()
# def devam_et():
#         print("Devam et fonksiyonu çalıştı.")
#         basla()


# basla()

# varsayılanolarak pythoniç içe fonksiyon çağırılırken en fazla 1000 defa çağırılabilir. Bu ayarı görmek ve değiştirmek için.

# import sys
# sys.getrecursionlimit(10000) # Bu değeri değiştirir.

# # parameter vs Argument
# # Parameter fonksiyon tanımlarken kulllanılır
# # Argument fonksiyon çağırılırken kullanılan bir tabirdir.

# def hesapla(isim): # parameter tanımladık
#     return isim

# hesapla("murat") # arguments tanımladık.

