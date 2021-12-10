# sayilar = (1,2,3,4,5,6,"merhaba", [1,2,3,4])

# for sayi in sayilar:
#     print(sayi)


# indeks = 0
# while indeks < len(sayilar):
#     print(sayilar[indeks])
#     indeks = indeks + 1

## range aralık kadar sayı üretir
# for i in range(1,10):
#     print(i)

# for t in "merhaba":
#     print(t)

# # sayılar liste değildir
# for i in 10:
#     print(i)

# # else for bittikten sonra çalışır

# for t in "merhaba":
#     print(t)
# else:
#     print("döngü bitti") 

# Dictionary lerde for kullanımı

# sozluk = {"a":1,"b":2,"c":3}

# # items fonksiyonu key value listesi doner
# print(sozluk.items())

# for key, value in sozluk.items():
#      print("key:" + key + " value:" + str(value))


# # listeden dönen elemının alt ögelerini ayrıştırmak için kullanılacak yöntem
# liste = [("1","2","3"),("a","b","c")]

# for a,b,c in liste:
#     print(a + b + c)

# # iki boyutlu listelerde dönmek için
# matris = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# for i in matris:
#     for j in i:
#         print(f"matris {i}, i nin elemanı {j}")

# metin = ""
# for i in matris:
#     for j in i:
#         metin = metin + str(j) + ","

# metin = metin[0:-1]
# print(metin)

# # 3 boyutlu listeler için 3 kez for yazılmalıdır.
# liste = [
#     [[1,2],[2,3]],
#     [[1,2],[2,3]],
#     [[1,2],[2,3]],
# ]

# for i in liste:
#     for j in i:
#         for k in j:
#             print(k)

# A = [[1,2,3],
#     [4,5,6]]

# B = [
#     [1,2],
#     [3,4],
#     [5,6]]

# result = [[0,0],
#           [0,0]]

# #iki matrisin çarpımı alınacak.
# #A * B = result (2*2 matris olacak)

# #A'nın satırları ile B'nin sütunları çarpım toplamı

# for ia in range(len(A)):
#     for ib in range(len(B[0])): 
#         for k in range(len(B)):
#             result[ia][ib] = result[ia][ib] + (A[ia][k] * B[k][ib]) 

# print(result)

import numpy as np

A = [[1,2,3],
     [4,5,6]]

B = [
     [1,2],
     [3,4],
     [5,6]]
    
An = np.array(A)
Bn = np.array(B)

result2 = np.dot(An,Bn)

print(result2)