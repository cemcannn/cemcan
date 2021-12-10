# Regular Expression : Düzenli İfadeler

metin1 = """merhaba murat nasılsın iyimin murat.cabuk@gmail.com ff@ @gffg oguz@fgfggf.com 
                 selim@dfdfdg.ca tugce@fgf.de dgdfgd@"""

for i in metin1.split(): # split fonksiyonu içini boş bırakırsan boşluk bulduğu yerden böler ve virgülle ayırır, başka bir ifade verirsen ifadeyi kaldırıp böler ve virgülle ayırır.
    if i == "murat": # Eğer i değişkeni eşitse "murat" string ifadesine:
        print("merhaba " + i) # "merhaba murat" olarak yazdır

print(metin1.find("murat")) #metin 1 içinde murat ifadesini bulup kaçıncı indekste olduğunu yazdırır.

print(metin1[8:14]) # metin1 içinde 8. indeksten 14. indekse kadar yazdırır 14 dahil değil.

for i in metin1:
    print(i)


#################################

metin = "merhaba nasılsın, iyi misin? herşey yolundadır umarım."


## Match Metodu kullanımı
print("################################# match Metodu #################################")

import re
result = re.match("merhaba",metin) # Match metodu bir karakter dizisinin yalnızca en başına bakar.
print(result) # match metodunu yazdırırsak 0-7 indeksleri arasında olduğunu ve içeriğini yazdırır.
print(metin[0:7]) # 0 ile 7 indeks arasını yazdır dersek "merhaba" string ifadesini yazdırır.

result = re.match("murat",metin)
print(result)

## Search Metodu
print("################################# search Metodu #################################")

metin = "python bir programlama dilidir"

nesne1 = re.search("python",metin) # ilgili metin içinde arama yapar.
print(nesne1) # Sonuç : python

nesne = re.search("(python) (bir) (programlama) (dilidir)",metin) 
print(nesne) # Sonuç : python bir programalama dilidir.

print(nesne.group()) # Sonuç : python bir programalama dilidir.
print(nesne.group(0)) # Sonuç : python bir programalama dilidir.
print(nesne.group(1)) # Sonuç : python 

## findall Metodu
print("################################# findall Metodu #################################")

import re

metin2 = "merhaba nasılsın, iyi misin? herşey yolundadır umarım. " \
        "herşey iyidir. iyi olsun zaten"

result=re.findall("iyi",metin2) #metin2 içinde geçen bütün "iyi" ifadelerini bulur.

print(result) # Sonuç : ['iyi', 'iyi', 'iyi']


print("################################# split Metodu #################################")

import re

metin = "merhaba nasılsın, iyi misin? herşey yolundadır umarım. " \
        "herşey iyidir. iyi olsun zaten"

result = re.split(" ",metin) # python içinde gömülü fonksiyon regular expression package ile de gelir, aynı görevi görür.

print(result) # Sonuç : ['merhaba', 'nasılsın,', 'iyi', 'misin?', 'herşey', 'yolundadır', 'umarım.', 'herşey', 'iyidir.', 'iyi', 'olsun', 'zaten']


print("################################# sub Metodu #################################")

import re

metin = "merhaba nasılsın, iyi misin? herşey yolundadır umarım. " \
        "herşey iyidir. iyi olsun zaten"

aranan_kelime = "iyi" # Değişecek ifade
yerine_gelecek_kelime = "mutlu" # Yerine gelecek ifade.

result = re.sub(aranan_kelime,yerine_gelecek_kelime,metin) # ifade değiştirmeye yarar

print(result) # Sonuç : merhaba nasılsın, mutlu misin? herşey yolundadır umarım. herşey mutludir. mutlu olsun zaten


print("################################# PATTERN KULLANIMI #################################")

# meta character dizileri
# [] . \* + ? {} ^ $ | ()

print("################################# [] Meta Character #################################")

metin = "merhaba nasılsın, iyi misin? herşey yolundadır umarım. " \
        "herşey iyidir. iyi olsun zaten" \
        " a1-2 cümle konuşalım"

aranan_kelime = "i[yds]i" # "i" başında olacak, "[ y d s]" harflerinden herhangi biri olacak sonra tekrar ""i"" geleck

result = re.findall(aranan_kelime,metin) # metin içindeki bütün aranan_kelime değişkenine bakılır.

print(result) # Sonuç : ['iyi', 'isi', 'iyi', 'iyi'] 
# "misin" deki "isi" dahi aldı.

result=re.findall("a[0-9]",metin)  # Şimdi rakamlarla deniyoruz, "a" ile başlayacak, 0-9 arası rakamlardan birini alacak herhangi bir ifade tüm metin içinde aratılır.

print(result) # Sonuç : ['a1']

result=re.findall("n[a-z]",metin) # "n" ile başlayacak ardından "a-z" arası bir harf gelecek.

print(result) # Sonuç : ['na', 'nd', 'nu']



print("################################# . Meta Character #################################")
# Bu metakarakter, yeni satır karakteri hariç bütün karakterleri temsil etmek için kullanılır.

metin = "merhaba nasılsın, iyi misin? herşey yolundadır umarım. " \
        "herşey iyidir. iyi olsun zaten i5a4i i5a6i"

aranan_kelime = "i.a6." # "i" ile başlayıp, herhangi bir ifade gelebilecek, "a" ve "6" ile devam edecek.

result=re.findall(aranan_kelime,metin) # metin içinde bütün aranan kelime değişkenine bakılır.

print(result) # Sonuç : ['i5a6i']


print("################################# * Meta Character #################################")
# Bu metakarakter, kendinden önce gelen bir düzenli ifade kalıbını sıfır veya daha fazla sayıda eşleştirir.

metin = "merhaba nasılsın, iyi misin? herşey yolundadır umarım. " \
        "herşey iyidir. iyi olsun zaten i5a4i i5a6i"

aranan_kelime = "da*" # kendinden önce gelen "a" yı alacak ya da 0 kabul edip almadan sadece "d" olanları alacak.

result=re.findall(aranan_kelime,metin)

print(result) # ['da', 'd', 'd']


aranan_kelime = "[ds][aıi]" # İlk olarak "d" ya da "s" ardından "a","ı","i" ifadelerinden biri gelecek.

result=re.findall(aranan_kelime,metin)

print(result) # Sonuç : ['sı', 'sı', 'si', 'da', 'dı', 'di']

aranan_kelime = "[ds][aıi]*" # İlk olarak "d" ya da "s" ardından "a","ı","i" ifadelerinden biri gelecek ya da hiçbiri gelmeyecek.

result=re.findall(aranan_kelime,metin)

print(result) # ['sı', 'sı', 'si', 'da', 'dı', 'di', 's']


print("################################# + Meta Character #################################")
# Bu metakarakter kendisinden önceki bir veya daha fazla sayıda tekrar eden karakterleri ayıklar. 

metin = "merhaba nasılsın, iyi misin? herşey yolundadır umarım. " \
        "herşey iyidir. iyi olsun dan zaten i5a4i i5a6i"

aranan_kelime = "da+" # "d" ile başlıyacak ardından "a" alacak fakat "*" meta karakteri gibi davranmayıp hepsini alacak.

result=re.findall(aranan_kelime,metin)

print(result) # Sonuç : ['da', 'da']


aranan_kelime = "da*"

result=re.findall(aranan_kelime,metin)

print(result) # ['da', 'd', 'd', 'da']


print("################################# ? Meta Character #################################")
# Bu metakarakter eşleşme sayısının sıfır veya bir olduğu durumları kapsıyor

yeniliste = ["st", "sat", "saat", "saaat", "falanca"]
for i in yeniliste:
    if re.match("sa*t",i):
        print(i) # Sonuç : ['st', 'sat', 'saat', 'saaat']

for i in yeniliste:
    if re.match("sa+t",i):
        print(i) # Sonuç : ['sat', 'saat', 'saaat']

for i in yeniliste:
    if re.match("sa?t",i):
        print(i) # Sonuç : ['st', 'sat']

# * : karakteri sıfır ya da daha fazla sayıda eşleşmeleri.
# + : karakteri bir ya da daha fazla sayıda eşleşmeleri kapsıyordu.
# ? : karakteri kendisinden önce gelen karakterin hiç bulunmadığı (yani sıfır sayıda olduğu) ve bir adet bulunduğu durumları içine alıyor.


print("################################# {} Meta Character #################################")
# Metakarakterimiz yardımıyla bir eşleşmeden kaç adet istediğimizi belirtebiliyoruz.

metin = "merhaba nasılsın, iyi misin? herşey yolundaaaddaadıır umarım. " \
        "herşey iyidir. iyi olsun dan zaten i5a4i i5a6i dl"

aranan_kelime = "[ds][aı]{2,3}[dlsrn]" # "d" ya da "s" ardından "a" ya da "ı" dan 2 ya da 3 tane ardından "d","l","s","r","n" ifadelerinden biri gelecek.

result=re.findall(aranan_kelime,metin)

print(result) # Sonuç : ['daaad', 'daad']


print("################################# ^ Meta Character ################################# ")
# Metakarakterinin iki işlevi vardır. Birinci işlevi, bir karakter dizisinin en başındaki veriyi sorgulamaktır. İkinci işlevi [] metakarakteri ile kullanılırsa hariç anlamına gelmektedir.

a = ['23BH56', 'TY76Z', '4Y7UZ', 'TYUDZ', '34534', '1agAY54']

# birinci gorev metnin başında arama yapmak
for i in a:
    nesne = re.search("^[A-Z]+[0-9]",i) # Metnin başında bir ya da birden fazla "A" ya da "Z" ardından "0" ya da "9" arayacak.
    if nesne: 
        print(nesne.group()) # Sonuç : ['TY7']

for i in a:
    nesne = re.search("^[A-Z]+[0-9].*",i) # Metnin başında bir ya da birden fazla "A" ya da "Z" ardından "0" ya da "9" ve ardından boşluk gelene kadar gelen bütün ifadeleri arayacak.
    if nesne:
        print(nesne.group()) # Sonuç : ['TY76Z']

# ikinci gorev [] meta character i içinde hariç anlamına gelir

for i in a:
    nesne = re.match("[0-9A-Z][^a-z]+",i) # Metnin içinde "0"dan "9"a kadar ya da "A"dan "Z"ye kadar ifadeleri arayacak ardından "a"dan "z"ye kadar hariç olanları arayacak.
    if nesne:
        print(nesne.group()) # Sonuç : ['1agAY54']


print("#################################  \ meta character #################################")
# Metakarakteri kaçış dizisidir.

liste = ["10$", "25€", "20$", "10TL", "25£"]

for i in liste:
    if re.match("[0-9]+\$",i): # Birden fazla "0" ya da "9" alır bunun metin sonunda aramaz, eğer öyle olsaydı para birimleri sonda olduğuiçin hiçbir veriyi çekemeyecekti.
        print(i) # Sonuç : 10$ , 20$


print("#################################  $ meta character #################################")
# Metakarakteri karakter dizilerinin nasıl biteceğini belirliyor.

liste = ["at", "katkı", "fakat", "atkı", "rahat",
"mat", "yat", "sat", "satılık", "katılım"]

for i in liste:
    if re.search("at$",i): # Sonu "at" olacak ifadeler
        print(i) # Sonuç : ['at'], ['fakat'], ['mat'], ['yat'], ['sat']

print("#################################  | meta character #################################")
# Metakarakteri birden fazla düzenli ifade kalıbını birlikte eşleştirmemizi sağlar.

metin = "merhaba nasılsın, iyi misin? herşey yolundaaaddaadıır umarım. " \
        "herşey iyidir. iyi merhaba olsun dan zaten i5a4i i5a6i dl \n" \
        "merhaba nasılsın? nasıl gidiyor?"

aranan_kelime = "^mer|or\?|i.i" # metnin başında mer ile başlayan ifade, "or?" ifadesi (soru işaretini metakarakter olarak algılamamsı için "\" kaçış karakterini kullandık, "i" gelecek ardından herhangi bir ifade ardından tekrar "i" gelecek. Bunların hepsi de "|" metakarakteri ile 3 adet arama yaptık.)

result=re.findall(aranan_kelime,metin)

print(result) # Sonuç : ['mer', 'iyi', 'isi', 'iyi', 'iyi', 'i i', 'idi', 'or?']


print("#################################  () meta character #################################")
# Metakarakter yardımıyla düzenli ifade kalıplarını gruplanır.

metin = "merhaba nasılsın, iyi misin? herşey yolundaaaddaadıır umarım. " \
        "herşey iyidir. iyi merhaba olsun dan zaten i5a4i i5a6i dl \n" \
        "sana 1-2 konu hakkında danışmak istiyorum. " \
        "merhaba nasılsın? nasıl gidiyor?"

aranan_kelime = "[a-z]+ h.+ d.+um\." # bir ya da birden fazla "a"dan "z"ye kadar ifade boşluk "h" ardından boşluk gelene bütün ifadeler sonra boşluk ardından "d" devamında bir ya da birden fazla herhangi biri ifade ardından "um" ardından "." 

result=re.findall(aranan_kelime,metin)

print(result) # Sonuç : ['konu hakkında danışmak istiyorum.']

aranan_kelime = "([a-z]+) (h.+) (d.+um\.)"

result=re.findall(aranan_kelime,metin) # Aynı işlemi gruplandırarak yapıyoruz.

print(result) # Sonuç : [('konu', 'hakkında', 'danışmak istiyorum.')]

aranan_kelime = "[a-z]+ |h.+ |d.+um\."

result=re.findall(aranan_kelime,metin)

print(result)


print("#################################  özel diziler #################################")

#- "\s" özel dizisi boşluk karakterlerini avlıyor
#- "\d" özel dizisi ondalık sayıları avlıyor
#- "\w" özel dizisi alfanümerik karakterleri ve "_" karakterini avlıyor. Yani [A-Za-z0-9_]

#Dedik ki, bir de bunların büyük harfli versiyonları vardır. İşte bu büyük harfli versiyonlar da yukarıdaki dizilerin yaptığı işin tam tersini yapar. Yani:

#- "\S" özel dizisi boşluk olmayan karakterleri avlar
#- "\D" özel dizisi ondalık sayı olmayan karakterleri avlar. Yani "[^0-9]" ile eşdeğerdir.
#- "\W" özel dizisi alfanümerik olmayan karakterleri ve "_" olmayan karakterleri avlar. Yani [^A-Za-z0-9_] ile eşdeğerdir.

metin_listesi = ["5 Ocak","27Mart","4 Ekim","Nisan 3"]

for i in metin_listesi:
    result = re.search("\d\s[A-Za-z]+",i) # Önce ondalık sayı olacak, ardından boşluk olacak, "A"dan "Z"ye kadar ya da "a"dan "z"ye kadar biri bir veya birden fazla olacak.
    if result:
        print(result.group()) # Sonuç : ['5 Ocak'],['4 Ekim']
# yukardaki ile aynı
for i in metin_listesi:
    result = re.search("[0-9] [A-Za-z]+",i) # Bu şekilde de yazılabilir.
    if result:
        print(result.group()) # Sonuç : ['5 Ocak'],['4 Ekim']


metin = "abc123_$%+" 
print(re.search("\w+",metin).group()) # Sonuç : ['abc123_']


metin = """esra : istinye 05331233445 esma : levent 05322134344 sevgi : dudullu
            05354445434 kemal : sanayi 05425455555 osman : tahtakale 02124334444
            metin : taksim 02124344332 kezban : caddebostan 02163222122"""

result = re.findall("(\w+)\s:\s(\w+)\s+(\d+)",metin) # önce bir veya birden fazla alfanumerik, boşluk, ":", boşluk, bir veya birden fazla alfanumerik, bir veya birden fazla boşluk, bir veya birden fazla ondalık sayı.

print(result) # Sonuç : [('esra', 'istinye', '05331233445'), ('esma', 'levent', '05322134344'), ('sevgi', 'dudullu', '05354445434'), ('kemal', 'sanayi', '05425455555'), ('osman', 'tahtakale', '02124334444'), ('metin', 'taksim', '02124344332'), ('kezban', 'caddebostan', '02163222122')]
