import random

rastgele_sayi = random.random()
print(rastgele_sayi)

rastgele_sayi2 = random.randint(1,1000) #random integer sayı getirir.
print(rastgele_sayi2)

secenekler = ["murat", "selçuk", "oğuz", "görkem"]
secenek = random.choice(secenekler) #Rastgele seçeneklerden çağrıyor.
print(secenek)

#üstteki ile aynı işi yapıyor.
random_sayi = random.randint(0,len(secenekler)-1)
print(secenekler[random_sayi])

#alttaki kod çalışmamaktadır çünkü dictionary lerde indeks yerine koy
secenekler = {"murat":"1", "selim":"2", "ahmet":"3"}
