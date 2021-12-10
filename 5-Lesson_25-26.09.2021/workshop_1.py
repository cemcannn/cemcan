# 1. Kullanıcıdan 2 değer alınacak.
# 2. rakam olup olmadıkları kontrol edilecek rakam değilse kullanıcı uyarılacak.
# 3. Rakamsa toplama işlemi yapılacak.
# 4. Kullanıcı uygulamada tutulacak, while kullanılmayacak, fonksiyon kullanılacak.
# 5. Çıkmak için seçenek sunulacak.

# deger1 = input("Birinci değeri giriniz : ")
# deger2 = input("İkinci değeri giriniz : ")

# toplama = 0
# if (deger1.isnumeric and deger2.isnumeric) == True:
#     toplama = deger1 + deger2

# secenek=input("""devam için "e", çıkmak için "h"ye basınız.""")
# if secenek == "h":
#     break

# def islem():
#     deger1 = input("Birinci değeri giriniz : ")
#     deger2 = input("İkinci değeri giriniz : ")
#     sonuc = 0
#     if (deger1.isnumeric() and deger2.isnumeric()) == True:
#         sonuc = int(deger1) + int(deger2)
#         sonuc = print("Sonucunuz :", sonuc, "Programdan çıkılıyor.")
#         return sonuc
#     else:
#         print("Lütfen rakam giriniz.")
#         basla()

# def basla():
#     secenek=input("""Çıkmak için "h"ye basınız, Devam etmek için herhangi bir tuşa basınız : """)
#     if secenek == "h":
#         return "Çıkış yapıldı"
#     else:
#         islem()

# islem()

# # 1. kullanıcıdan 2 değer alınacak
# # 2. rakam olup olmadıkları kontrolu yapılacak rakam değilse kullanıcı uyarılacak
# # 3. rakamsa toplama işlemi yapılacak sonuç gösterilecek
# # 4. kullanıcı uygulamada tutulacak (while kullanılmayacak, fonksiyon kullanılacak)
# # 5. çıkmak için seçenek sunulacak
 
# # fonksiyondan çıkmak istenildiğinde return komutu kullanılır
# # return çalıştığı an return altında kod varsa onlar çalıştırılmaz
 
# def isleme_basla(): # lider fonksiyon, karar verici
#     sayi1 = input("sayi1 giriniz: ")
#     sayi2 = input("sayi2 giriniz: ")
 
#     degeler_sayi_mi = degerleri_kontrol_et(sayi1, sayi2)
 
#     if degeler_sayi_mi==True:
#         sonuc = toplama_yap(sayi1,sayi2)
#         print(sonuc)
#     else:
#         print("lütfen sayı giriniz")
 
#     secenek = input("devam (e), çıkmak (h): ")
#     if secenek == "h":
#         return # bir nevi break yapıyoruz
#     else:
#         isleme_basla()
    
# def degerleri_kontrol_et(sayi1, sayi2):
#     sayi_degerleri_rakam_mi = True
#     if sayi1.isnumeric() == False or sayi2.isnumeric() ==False:
#         sayi_degerleri_rakam_mi =  False
#     return sayi_degerleri_rakam_mi
 
# def toplama_yap(sayi1,sayi2):
#     return int(sayi1) + int(sayi2)
 
# isleme_basla()
 
# # diğer bir yazım şekli
 
# def isleme_basla(secenek): # lider fonksiyon, karar verici
#     sayi1 = input("sayi1 giriniz: ")
#     sayi2 = input("sayi2 giriniz: ")
 
#     degerleri_kontrol_et(sayi1, sayi2, secenek)
 
    
# def degerleri_kontrol_et(sayi1, sayi2,secenek):
 
#     if sayi1.isnumeric() or sayi2.isnumeric():
#         if secenek == "T":
#             toplama_yap_sonucu_goster(sayi1,sayi2)
#         else:
#             carma_yap_sonucu_goster(sayi1,sayi2)
#     else:
#         print("lütfen sayı giriniz")
#     secenek_sun()
    
 
# def toplama_yap_sonucu_goster(sayi1,sayi2):
#     print(int(sayi1) + int(sayi2))
#     secenek_sun()
 
# def carma_yap_sonucu_goster(sayi1,sayi2):
#     print(int(sayi1) * int(sayi2))
#     secenek_sun()
    
 
# def secenek_sun():
#     secenek = input("kalmak için (e), çıkmak için (h): ")
#     if secenek == "e":
#         isleme_basla()
#     else:
#         pass


 
# isleme_basla("T")


