############################################ Lambda Fonksiyonu #########################

## lambda fonksiyonu -> anonymous functions
# kullanımı
#FonksiyonAdi = lambda paremetre1,paremetre2: dönüş değeri
#fonk = lambda param1, param2: param1 + param2

# klasik yazım
def topla(x):
    return x + 1

a = topla(3)
print(a)

# lambda kullanımı

topla_lambda = lambda x:x+1
print(topla_lambda(4))

print((lambda x,y:x*y)(2,5))

## geriye fonksiyon dondureen fonksiyon, yada parametre olarak fonksiyon alan fonksiyonlar

# func burada bir fonksiyonu ifade eder
def iki_defa_calistir(func):
    def sonuc(x):
        return func(func(x))  #  ((10 * 2) * 2)  // print(carp(carp(10)))
    return sonuc

def carp(x):
    return x * 2

calistir = iki_defa_calistir(carp)
print(calistir(10))

# lambda versiyonu

iki_defa_calistir_lambda = lambda x,f:x * f(x)
calistir_lambda = iki_defa_calistir_lambda(11,lambda x: x*2)
print(calistir_lambda)

# en kısa yazım
print((lambda x,f:x * f(x))(11,lambda x: x*2))

# lambda if kullanımı

# klasik yazım

def test_mod(x):
    if x%2==1:
        return "tek sayı"
    else:
        return "çift sayı"

print(test_mod(2))
print(test_mod(5))


# one line if kullanımı

secenek = True
print(test_mod((2 if secenek== True else 5)))

# lambda ile if kullanarak
test_mod_lambda= lambda x: "tek sayı" if x%2==1 else "çift sayı"
print(test_mod_lambda(2))

# lambda ile en kısa hali
print((lambda x: "tek sayı" if x%2==1 else "çift sayı")(5))

# lambda ile içi içe if kullanımı

test_mod_lambda_nested_if= lambda x: "tek sayı" if x%2==1 else ( "rakam=3" if x==2 else "rakam başka bir sayı" )
print(test_mod_lambda_nested_if(5))
print(test_mod_lambda_nested_if(4))

############################################ Map Fonksiyonu #########################
# kullanımı
# map(function_to_apply, list_of_inputs)

liste = [1,2,3,4,5]
liste_karesi=[]

for i in liste:
    liste_karesi.append(i**2)
print(liste)
print(liste_karesi)

# map ile yazımı

def karesini_al(x):
    return x**2
liste_map = [1,2,3,4,5]
liste_karesi_map = list(map(karesini_al, liste_map))

print(liste_map)
print(liste_karesi_map)

# lamda ile map kullanımı
liste_lambda_map = [1,3,5,7,9]

liste_lambda_map_karesi = list(map(lambda x: x**2, liste_lambda_map))
print(liste_lambda_map)
print(liste_lambda_map_karesi)
# en kısa yazım
print(list(map(lambda x: x**2, [2,4,5])))

# fonksiyon ile kullanımı
def karmasik_islemler(x):
    return x * 2 - 1 / (3-4)

print(list(map(karmasik_islemler, [2,4,5])))

# string ile kullanım

metinler = [["ahmet","mehmet"],["ali","kemal","veli"],["1","2","3"]]

def liste_dondur(liste_parametresi):
    liste = []

    if len(liste_parametresi)==2 and type(liste_parametresi[0])==str:
        for t in liste_parametresi:
            liste.append(t.upper())

    elif len(liste_parametresi) > 2 and (liste_parametresi[0]).isnumeric() == False:
        for t in liste_parametresi:
            liste.append("merahaba "+ t)
    else:
        for t in liste_parametresi:
            liste.append(int(t) * 2)

    return liste

print(list(map(liste_dondur,metinler)))

## map karmaşık ornek

func_listesi_map = [lambda x: x+x, lambda x: x*x]
for i in range(5):
    value = list(map(lambda y:y(i),func_listesi_map))
    print(value)

## list comprehension yazımı
print("list comprehension")
print([(x+x,x*x) for x in range(5)])


######################################################  Filter  ################################
# kullanımı
# filter(function, iterable)

isim_listesi= ["murat","ali","mehmet","ahmet","zeki","abdullah"]

def kelime_a_harfi_ile_mi_basliyor(x):
    return x[0]=="a"

print(list(filter(kelime_a_harfi_ile_mi_basliyor,isim_listesi)))

# filter lambda kullanımı

print(list(filter(lambda x: x%2==0,range(1,20))))

# list comprehension versiyonu
print([x for x in range(20,40) if x%2==0])

## ############################################# reduce   ##################3

# kullanımı
# reduce(function, iterable)

from functools import reduce

numaralar = [11,3,45,67,100,1,0,23,78,4]

def buyuk_rakam(a,b):
    if a > b:
        return a
    return b

print(reduce(buyuk_rakam,numaralar))

# lambda ile kullanım

print(reduce(lambda a,b: a if a>b else b,[11,3,45,67,100,1,0,23,78,4]))

# reduce ile toplama

numaralar_toplama = [11,3,45,67,100,1,0,23,78,4]
def reduce_topla(a,b):
    return a+b
print(reduce(reduce_topla,numaralar_toplama))


# reduce string kullanımı
metinler_cumle = ["merhaba", "murat", "nasılsın", "?"]

def cumle_birlestir(a,b):
    if b != "?":
        return a+ " " +b
    else:
        return a+b

print(reduce(cumle_birlestir,metinler_cumle))


############################################# ZIP ################################

a = [1,2,3]
b = ["a","b","c"]
c = ["/","+","*"]

d = list(zip(a,b,c))
print(d)


f = [1,2]

g = list(zip(a,f))
print(g)

from itertools import zip_longest

g = list(zip_longest(a,f,fillvalue=False))
print(g)

############################################ groupby ###################################

from itertools import groupby

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]

for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print("A %s is a %s." % (thing[1], key))
    print("")













































