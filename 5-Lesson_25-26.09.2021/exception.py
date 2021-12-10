# logical error

# Syntax error: yazım hatası
# if 1==1 # iki nokta üstüste unutulmuş
#     print("merhaba")

# print(dir(locals()['__builtins__'])) #Error types

# try : hata vermesi muhtemelkod bloğu  için kullanılır.
# except : patlayan hatanın patlamamasını sağlayarak hata durumunda yapılacak işlemlerin olduğu blok
# else : try bloğu hata vermeden çalışırsa kullanılacak blok.
# finally : hata olsa da olmasa da çalışacak blok.

# örnek uygulama

# sayi1 = int(input("Sayı 1'i giriniz"))
# sayi2 = int(input("Sayı 2'yi giriniz"))

# try:
#     print("bölüm", sayi1/sayi2)
# except:
#     print("bir hata oluştu.")
# else:
#     print("doğru değerler verdiniz, teşekkürler.")
# finally:
#     print("Hata olsun olmasın çalıştı")



# while True:
#     sayi1 = input("Sayı 1'i giriniz : ")
#     sayi2 = input("Sayı 2'yi giriniz : ")    
#     try:
#         sayi1 = float(sayi1)
#         sayi2 = float(sayi2)
#         print(sayi1/sayi2)
#     except TypeError:
#         print("Lütfen iki değeride rakam olarak giriniz.")
#     except ValueError:
#         print("Lütfen iki değeride rakam olarak giriniz.")
#     except ZeroDivisionError:
#         print("Lütfen bölen sayıyı sıfır değeri girmeyiniz.")
#     except:
#         print("Tanımlanamayan hata oluştu, tekrar deneyiniz.")
#     finally:
#         secenek=input("""devam için "e", çıkmak için "h"ye basınız.""")
#         if secenek == "h":
#             break
# print("program çalıştı")

# sayi = input("Sayi giriniz : ")

# if sayi.isnumeric() == False:
#     raise Exception("Sayı girmediniz!")

# isim = input("İsim giriniz : ")

# if isim == "Murat" or "murat":
#     raise Exception("Muratlar giremez.")
# else:
#     print(f"Merhaba ey {isim}")

