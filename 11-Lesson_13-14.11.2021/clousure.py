def mesaj_yaz(isim:str):
    def yaz():
        print("merhaba " + isim)
    yaz()

mesaj_yaz("murat")


def mesaj_yaz2(isim:str):
    def yaz():
        print("merhaba " + isim)
    return yaz

f = mesaj_yaz2("murat")
print(f)
f()

### iç içe çarpma fonksiyon kullanımı

def carpma_yap(i):
    def carp(x):
        return i * x
    return carp

verilen_sayiyi_3_ile_carp = carpma_yap(3)
verilen_sayiyi_5_ile_carp = carpma_yap(5)

print(verilen_sayiyi_3_ile_carp(10))


## iç içe toplama
def toplama_yap(n):
    def topla(x):
        def yine_topla(y):
            return n+x+y
        return yine_topla
    return topla

print(toplama_yap(2)(3)(4))

verilen_sayiyi_5_ile_topla= toplama_yap(5)
verilen_sayiyi_5_ve_3_ile_topla = verilen_sayiyi_5_ile_topla(3)
print(verilen_sayiyi_5_ve_3_ile_topla(6))

















