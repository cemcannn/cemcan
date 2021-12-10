liste = [1,2,3,4,[1,2,3,4],6,7,8]
liste2=[]

for i in liste:
    if type(i)==list:
        for t in i:
            liste2.append(t)
    else:
        liste2.append(i)


print(liste2)

# list comprehension kullanımı
# new_list = [expression for member in iterable]
# new_list = [expression for member in iterable (if conditional)]

liste5 = []
for x in range(1,11):
    liste5.append(x**2)

# list comprehension  şekli
liste3 = [x**2 for x in range(1,11)]

print(liste3)


# sadece çift rakamların karesi

liste6 = [x**2 for x in range(1,11) if x%2==0]
print(liste6)

# nested (iç içe listeler)

liste7 = [[1,2,3],[4,5,6],[7,8,9]]


                #xpression   # birinci (dış) for  # ikinci (iç) for
liste7_flat_liste = [x**2 for i in liste7 for x in i]
print(liste7_flat_liste)

#for i in a:
#    for t in i:


                        # xpression      # for dongü kısmı
liste7_nested_liste = [[x**2 for x in i] for i in liste7]
print(liste7_nested_liste)

#for i in a:
#    return list


liste_matrix = [
    [0,0,0,0,0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


liste_matrix_comp = [[0 for x in range(1,6)] for i in range(1,6)]

print(liste_matrix_comp)

liste_matrix_normal =[]
for i in range(1,6):
    liste = [0,0,0,0,0]
    liste_matrix_normal.append(liste)

print(len(liste_matrix_normal))
print(liste_matrix_normal)


# üçlü bir örnek yapalım

#matrix = [
#         [[1,2,3],    [1,2,3],    [1,2,3]],
#         [[1,2,3],    [1,2,3],    [1,2,3]],
#         [[1,2,3],    [1,2,3],    [1,2,3]]
#         ]

# liste = [expression for i in iterator]

liste3_elaman_sayisi = 3
liste2_elaman_sayisi = 3
liste1_elaman_sayisi = 3

matrix3 = [ [[c for c in range(1,liste1_elaman_sayisi +1 )]
                    for i in range(1,liste2_elaman_sayisi +1)]
                        for t in range(1,liste3_elaman_sayisi + 1)]
print(matrix3)


okul = [ [[c for c in range(1,liste1_elaman_sayisi +1 )]
                    for i in range(1,liste2_elaman_sayisi +1)]
                        for t in range(1,liste3_elaman_sayisi + 1)]

butun_ogrenciler = [ogrenci for sinif in okul
                         for ogrenciler in sinif
                            for ogrenci in ogrenciler]

liste_nested = []

for i in range(1,4):
    for t in range(1,4):
        liste_nested.append(list(range(1,4)))

print(liste_nested)

print(butun_ogrenciler)


# list comrehension aritmetik

matrix4 = [[[1,2,3]] * 3] * 3

print(matrix4)


liste8 = [((lambda x: x / 2)(i)) for i in range(4)]

print(liste8)



