# Best practice keywordleri he zaman kullanmaya çalışın

# Special Parameters

#Variable length arguments

#Arbitrary keyword argument

def cok_sayi_topla(*args): # İçeriği tuple cinsinden veriyor.
    i = 0
    for sayi in args:
        i =i+ sayi
    print(i)

cok_sayi_topla(1,2,3,4,5)

## Arbitrary keywords argument

def farkli_topla(**kwargs):
    print(type(kwargs))

farkli_topla()

def farkli_topla(sozluk):
    sonuc=["",0,0]
    for key in sozluk:
        if key=="kelimeler":
            for kelime in sozluk[key]:
                sonuc[0]=sonuc[0] + " " + kelime
        elif key == "sayilar":
            for sayi in sozluk[key]:
                sonuc[1] = sonuc[1] + sayi
        else:
            sonuc[2] = sonuc[2] + 1
    print(sonuc)        

farkli_topla({"kelimeler":("merhaba","murat","nasılsın"),"sayilar":(1,2,3,4,5)})
