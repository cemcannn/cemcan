# decorator

def mesaj_getir(i):
    def birinci_mesaj():
        return "ben birinci mesajım"

    def ikinci_mesaj():
        return "ben ikinci mesajım"

    if i == 1:
        return birinci_mesaj
    else:
        return ikinci_mesaj


birinci_mesaj = mesaj_getir(1)
ikinci_mesaj = mesaj_getir(2)

print(birinci_mesaj())
print(ikinci_mesaj())


# clousure dan decorator a geçiş

def my_decorator(func):
    def wrapper():
        print("fonksiyon çağrılmadan once çalıştım")
        func()
        print("fonksiyon çağrıldıktan sonra çalıştım")
    return wrapper

# def mesaj_ver():
#    print("merhaba")

#test_decorator = my_decorator(mesaj_ver)
# test_decorator()


# pie syntax
print("-------------------  decorator olarak çalıştırılıyor")


@my_decorator
def mesaj_ver2():
    print("merhaba2")


mesaj_ver2()


# decorater ile parametre alıp

def do_twice(func):
    # * keywordsuz parametreler, ** keywordlu parametreler
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


print("-------------------------------")


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


print(return_greeting("Adam"))


# property

class Ogrenci:
    _ogrenciler = []  # yarı gizli öğe

    def __init__(self, isim):
        self._isim = isim  # yarı gizli öğe
        self.ogrencilere_ekle()

    def ogrencilere_ekle(self):
        self._ogrenciler.append(self._isim)
        print('{} adlı öğrenci öğrenci listesine eklendi'.format(self._isim))

    @classmethod
    def ogrencileri_goruntule(cls):
        print('Öğrenci listesi:')
        for ogrenci in cls._ogrenciler:
            print(ogrenci)

    @property
    def isim(self):
        return "merhaba " + self._isim

    @isim.setter
    def isim(self, yeni_isim):

        if yeni_isim.isnumeric():
            raise Exception("Lütfen String Giriniz")
        ogrenci = self._ogrenciler.index(self._isim)
        self._ogrenciler[ogrenci] = yeni_isim
        print('yeni isim: ', yeni_isim)


ogrenci1 = Ogrenci("Murat")

print(ogrenci1.isim)
ogrenci1.isim = "Mehmet"

ogrenci1.isim = 1
