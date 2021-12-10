#list [1,2]
#tuple (1,2)
#dict {1:"11","merhaba":2}
#set {1,2,3,4}

#setleri n her bir elemanı unique (tekil, eşsiz)

kume={1,2,3,4,4,4,4}
print(kume)

kume1 = {4,5,6,7,1,2} #setlerde yazdırırken sıraya dizer
kume2 = {7,4,2,11,"merhaba"}
kume3=kume1.union(kume2) # kümeleri birleştirme, birleştirirken de aynı olanları teke indiriyor sonra sıraya diziyor.
print(kume3)

kume_kesisim=kume1.intersection(kume2) #kume 1 ve kume2 kesişimleri
kume_fark=kume1.difference(kume2) #kume1 in kume2 den farkı

kume_sim_fark=kume1.symmetric_difference(kume2) #simetrik fark alıyor, yani kesişim hariç a ve b kumesinde olanlar.

#silme
kume1.pop() # setler aradan çıkarma yapmaz yani parantez için sayı almaz. sondan çıkarma yapar sadece

#değiştirme
#kume[4]=100 #değiştirme yapılmaz

#ekleme
#kume1.append[20] ekleme yapılamıyor

