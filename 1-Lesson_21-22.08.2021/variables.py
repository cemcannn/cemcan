import os

# Variables yorum satırıdır buraya istediğimizi yazabiliriz. Bizden sonra gelecek birdevveloper olursa onu bilgilendirmek kendimizi bilgilendirmek gibi.
# TODO : daha sonra düzenlecek alanları kullanmamız için gerekli olur, daha sonrasında todo bölümüne girip yapılacak işaretlere bakıyoruz. Nerelere ne yazdım neler düzelecek gibi.


print('Hello World')
print("Hello World")

# Kod Kısayolları
# Seçili alanı yorum satırına almak (ctrl + K + C)
# Seçili alanı yorum satırından almak (ctrl + K + U)
# WorldWrap, metni satır sonundan itibaren alta götürür, bir nevi metnikaydır (alt + Z)
# Kodları düzenleme (Shift + Alt + F)
# Değişken tanımlama kuralları
# 1) Değişken ismi, kesinlikle iki kelimeden oluşamaz
# Örnek,
# benim adım = "cem can"
# burada benim kısmını değişken olarak algılar-
# Eğer değişken ism birden fazla kelimeden oluşacak ise, izin verilen özel karakter (_) ile ayrılmalıdır veya CamelCase mantığı ile verilmelidir. Not: değişken ismi küçük harf ile başlar (Kati kural değildir. Global kabul görmüş kuraldır.)
# Örnek kullanım şekilleri
#   1.1) benim_adim = "Cem Can"
#   1.2) benimAdim = "cem can"

# 2) Değişken ismi, kesinlikle tanımlı kelimeden oluşamaz
# print = "cem can"
# print(print)

# 3) Lütfen Türkçe karakter kullanmayınız
#   Örnek kullanım,
#   kullanıcıAdi = "admin" => Hatalı kullanım
#   kullaniciAdi = "admin" => Doğru kullanım

# 4)   Değişken içerisinde, özel karakter kullanmayın
# $ulke = "Türkiye"

# 5) Değişken ismi sayı ile başlayamaz
# 1ogrenci = "Cem" => hatalı kullanım
# ama o1ogrenci = "Cem" => doğru kullanım
# ogrenci1 = "cem" => doğru kullanım

# Değişken tanımlama şekli
# değişkenAdi = değişkenDeğeri
isim = "Cem"
il = "İzmir"
mail = "cmcan@windowslive.com"

print(mail)

mail = mail + " - bilgeadam"
print(mail)

# global alan değişken tanımlama
firstName = "Cem"
lastName = "Can"
phone = "+905557863545"
mail = "cmcan@windowslive.com"
age = 90

# Yukarıda tanımladığımız değişken tipleri metinsel (string) veri türleridir

# C# Değişken tanımlama şekli

# int sayi = 1;
# long sayi1 = 213123;
# string adim = "Cem Can"

# def Deneme():
#     denemeVariable = ""
#     pass

# def Denemedim():
#     denemedimVariable = ""
#     pass

# def Deneyebilirim():
#     deneyebilirimVariable = ""
#     pass

# sayısal veri tipleri

# int, long ve float

os.system('cls')

sayi = 1
ondalikli = 12.9

print(sayi)
print(ondalikli)
print(type(sayi))
print(type(ondalikli))

os.system('cls')


print(firstName)
print(lastName)
print(mail)
print(phone)

# print içerisinde var olan değerleri (,) ile ayırırsanız aralarında bir boşluk bırakacaktır.
print(firstName, lastName, mail, phone)

print(firstName, lastName, mail, phone, sep='/')

# (+) operatörü => eğer string değerler içerisinde kullanırsanız araç görevi görecektir yani metin birleştirme işlemi yapacaktır.

print(firstName + lastName + mail + phone)

print(firstName + " " + lastName + " " + mail + " " + phone)

os.system('cls')
print(firstName, lastName, mail, phone, age)
# print(firstName + lastName + mail + phone + age) => hatalı kullanım "age" integer olarak algılayıp string ile toplayamıyor.
# print(firstName + " " + lastName + " " + mail + " " + phone + " " + age) => aynı şekilde hatalı kullanım "age" integer olarak algılayıp string ile toplayamıyor.
print(firstName + " " + lastName + " " + mail + " " + phone + " " + str(age))

os.system('cls')

# Mantıksal Veri Türü

# result = False
# retVal = "bugün hava güneşli mi?" => true, false
# print(result)

result = 10 > 8
print("işlem sonucu :", result)
print(type(result))

print(firstName + "\n"+lastName)
# \n => bir alt satıra geç (new line)

os.system('cls')
print("cem can\n" * 500)
# toplamda 500 defa adını yazdır, yazdırdıktan sonra bir alt satıra geç.

os.system('cls')

print("bilge\nadam\npython\ndersleri")

os.system('cls')
print("""
-------------------------------------Bilge Adam---------------------------------
-
-
-
-
-
-----------------------------Bilge Adam Telefon Rehberi-------------------------
-
-
-
-
--------------------------------------------------------------------------------
""")
