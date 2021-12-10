import os

# liste []
# tuple ()
# dictionary mutable dır, değişkendir.

sozluk = {1:"bir",2:"iki",3:"üç"}
print(sozluk)

sozluk2= {1:"bir",2:"iki", 3:"üç","sayilar":[1,2,3,]}
print(sozluk2)

sozluk3= {1:"bir",2:"iki", 3:"üç", "sayilar":[1,2,3], "abc":"def", "merhaba":1, 1:5} #son key dğeri iki defa girildiği için ilk key değerini iptal etti yazdırırken.
# print(sozluk3)
# print(sozluk3[1]) # Direkt key değerini yazdırır.
# print(sozluk3["sayilar"][0])
# sozluk3["sayilar"][0]=[5]
# print(sozluk3)

# sozluk5 = dict([(1,"bir"),("beş",5)])
# print(sozluk5.get(1)) #key değerinin karşılığını yazdırır, key error vermez

print(sozluk3.values()) # Value değerlerini karşılığını yazdırır.

print(sozluk3.keys()) # Key değerlerini yazdırır

print(sozluk3.items()) # Key ve Value değerlerini karşılıklı yazdırır.

sozluk6 = {1:1,2:2,3:3}
print(sozluk6)

#value değerlerini değiştirmek

sozluk6[2]="iki"
print(sozluk6)
print(sozluk6.get(2))

#ekleme
sozluk6[4]="dört"
print(sozluk6)

#silme
sozluk6.pop(4)
print(sozluk6)

#bütün değerleri silme
sozluk6.clear()

#bir şeyi tamamen memory dn uçurmak için
del sozluk6


os.system ("cls")

sozluk7={1:1,2:2}
sozluk7={} # içini bu şekilde de silebiliriz
print(sozluk7)

sozluk8={1:{1:"bir",2:"iki"},2.1:[1.,2,3,{1:2,"wew":4}]}
print(sozluk8)

sozluk8= {1:["bir",1],2:"iki", 3:"üç","sayilar":[1,2,3,]}
print(sozluk8[1][0])

