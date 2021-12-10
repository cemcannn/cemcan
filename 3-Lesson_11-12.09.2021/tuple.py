#Tuple veri inmutable dır, sabittir, değiştirilemez.
#tuplelara veri eklenemez veri çıkarılamaz
#arama yapılabilir

mytuple=(1,2,3,4,5,"elma",[1,"2"],"a",True)
print(mytuple[2]) #3. eleman çağırılabilir.

#mytuple.pop() #sayı çıkarılamaz

print(mytuple[1:3]) #2'den 3'e kadar yazdırır

print(mytuple.count(2)) #sayma yapar

print(len(mytuple)) #uzunluk ölçer

liste = mytuple[6] #tupple ın içindeki listeyi bir listeye atayıp, sayı eklersek ekler ve bunu tuple içinde de ekler.

print(type(liste))

liste.append(2)
print(liste)
print(mytuple)

mytuple[6].append(8) #bu şekilde tupple içindeki listeye 8 sayısı eklenebiliyor.

mytuple2=(1,6,3,4,5)
print(sorted(mytuple2)) #bu fonksiyon tuple sıralı olarak gösterir fakat tuple yine aynı kalır.
print(mytuple2)

