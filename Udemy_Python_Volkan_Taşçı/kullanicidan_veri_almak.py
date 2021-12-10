isim = input("İsminizi giriniz : ") #İnput kullanıcıdan veri alır.
print("isminiz : ",isim)

x = 5
y = input("sayı giriniz") #her zaman kullanıcıdan veriyi string olarak alır.
print(x + int(y))

#Hesap makinesi uygulaması

sayi1 = float(input("Birinci sayıyı giriniz :"))
sayi2 = float(input("İkinci sayıyı giriniz  :"))

print("\n")
print("Toplama sonucu   :", sayi1 + sayi2)
print("Çıkarma sonucu   :", sayi1 - sayi2)
print("Çarpma sonucu    :", sayi1 * sayi2)
print("Bölme sonucu     :", sayi1 / sayi2)

a = float(input("Birinci sayıyı giriniz :"))
b = int(input("İkinci sayıyı giriniz  :"))

print(bool(a)) #bool sana girilen verinin doğru türde veri olup olmadığını söyler.