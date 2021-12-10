import time

# time modülünün içindekileri görmek için
for i in dir(time):
    print(i)

# time modülü içinde sleep fonksiyonu
print("merhabalar efendim")
time.sleep(2) # 2 saniye gecikme ile alttaki string ifadeyi yazdırır.
print("hoşgeldiniz")

# time modülü içinde time fonksiyonu
zaman1 = time.time()
time.sleep(2)
zaman2 = time.time()

print("fark : {}:".format(zaman2 - zaman1)) #2 saniye sonra yazdırdığımız zaman ile aradaki farkı yazdırıyoruz.
