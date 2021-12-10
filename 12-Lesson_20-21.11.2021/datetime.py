import time # time modülü import ediyoruz.  
import datetime #datetime modülü import ediyoruz.
import locale #locale modülü ile bölgesel ayar yapıyoruz.

print("""
---------------strftime biçimlendiricileri---------------
%a - hafta gününün kısaltılmış adı
%A - hafta gününün tam adı
%b - ayın kısaltılmış adı
%B - ayın tam adı
%c - tam tarih, saat ve zaman bilgisi
%d - sayı değerli bir karakter dizisi olarak gün
%j - belli bir tarihin, yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı
%m - sayı değerli bir karakter dizisi olarak ay
%U - belli bir tarihin yılın kaçıncı haftasına geldiğini gösteren 0-53 arası bir sayı
%y - yılın son iki rakamı
%Y - yılın dört haneli tam hali
%x - tam tarih bilgisi
%X - tam saat bilgisi
--------------------------------------------------------
""")

zaman = time.strftime("%a, %d %b %Y %H:%M:%S") #time modülünün strftime fonksiyonunda yukarıdaki biçimendirileri girerek (haftanın günü, gün, ay, yıl, saat, dakika, saniye)
print(zaman) #Değişkeni yazdırıyoruz.

print("----------------------------------------------- Bölgesel dil için")

for lang in locale.windows_locale.values(): # Bölgesel dil listesini bu şekilde açabiliyoruz
    print(lang)

locale.setlocale(locale.LC_TIME,"tr_TR") # Ülkeyi ayarlamak için kullanıyoruz.

print("----------------------------------------------- Bulunduğumuz zaman için")

an = datetime.datetime.now()

print(an)

# print(su_an.year)

# print(su_an.month)

# print(su_an.day)

# print(su_an.weekday())

# print(su_an.minute)

# print(datetime.datetime.ctime(su_an))
