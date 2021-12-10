import os

# liste []
liste=[1,2,3,4,"merhaba","a",[1,2,3,4,["merhaba","a",1,2]],12.3] #listeler bu şekilde olabilir.
print(liste)

#Diziler indexi 0'dan başlar.

print(liste[0])

duzenli_liste = [[1,2,3],
                [4,5,6,[1,2,3]],
                [7,8,9]]
#eğer düzenli listede 1. elemanı yazdırmak istersen liste yazdırır.           
print(duzenli_liste[0])
#eğer düzenli listede 2. elemanın 2. elemanını yazdırmak istersen
print(duzenli_liste[1][1])
#eğer düzenli listede 2. elemanın 4. elemanının 2.elemanını yazdırmak istersen
print(duzenli_liste[1][3][1])

## listenin son elemanına erişmek için -1
print(liste[-1])
print(liste[1:3]) # 2. ile 3. elemanı kadar alıyor, 4. elemanı dahil etmiyor.
print(liste[:-2]) #baştan -2. elemana kadar alıyor
print(liste[0:]) #0'dan başla nereye kadar giderse
print(liste[:]) # tamamını alır

liste.append("a") # listenin sonuna "a" ekler
print(liste)

liste.extend([1,2,3]) # listenin sonuna liste ekler fakat elemanları ayrı ayrı ekler, eğer append ile ekleseydik listeyi olduğu gibi ekleyecekti.
print(liste)

liste3= ["a","b","c","d"]
print(liste3*2) #listeyi iki ile çarpar.

del liste3[0] #listede 1. elemanı siler.
print(liste3)

liste4=["a","b","c","d"]
del liste4[1:-1] #1'den -1'e kadar siler.
print(liste4)

liste5=[1,2,3,4,5,5,5,6,7,8,"p","y"] 
liste5.remove(2) #sadece 2 elemanını siler listeden
print(liste5)

os.system ("cls")

liste5.pop() #pop boş bırakılırsa listedeki son elemanı siler yani LİFO, index girersen o sıradaki sayıyı siler.
print(liste5)

os.system ("cls")

print(liste5.count(5)) #listede kaç defa 5 varsa sayar.

liste6=["a","c","m","zen","cem"]
print(liste6.sort()) #listenin sıralanmasını sağlar, listenin içinde string ve integer ifadeler karışıksa sıralama yapmaz.

liste7=[2,5,6,3,7,9]
liste7.sort()
print(liste7)

#workshop
# kullanıcıdan 3 rakam alınacak
# rakamlar küçükten büyüğe sıralanacak.
# kullanıcıdan bir index değeri alınarak listeden ilgili indexe gelen değer silinecek (liste ekrana yazdırılacak)
# listenin uzunluğu ekrana yazdırılacak

os.system ("cls")

sayi_1 = int(input("Birinci rakam giriniz : "))
sayi_2 = int(input("İkinci rakamı giriniz : "))
sayi_3 = int(input("Üçüncü rakamı giriniz : "))

liste8=[sayi_1, sayi_2, sayi_3]
liste8.sort()
print(liste8)
index = int(input("0 ile 2 arasında bir index değeri giriniz : "))
liste8.pop(index)
print(liste8)
print("liste eleman sayısı : {}".format(len(liste8)))