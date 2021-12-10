# class ve orneklem niletiklerine erişmesi gerekmeyen metodlar için kullanılır


class Insan:
    isimler = [] # class attribute (nitelik)
    def __init__(self, isim):
        self.isim = isim # (orneklem yani instance attribute (nitelik))
        self.isimler.append(isim)
        self.liste = []
    
    def isim_yaz(self): # orneklem metodu
        print(self.isim)
    
    @classmethod
    def isimleri_yazdir(cls): # class metodu
        print(cls.isimler)

    @staticmethod
    def yas_hesapla(dogum_yil, suanki_yil): # ne calass nede orneklem (instance) niteliklerine erişebilir, ikisine de erişemez
        print(suanki_yil - dogum_yil)



murat = Insan("murat")
murat.liste.append(["fsdfsdf",["fgdfdf","sfsdf",["sdsd"]]])

selim = Insan("selim")

print(Insan.isimleri_yazdir())

Insan.yas_hesapla(1980,2021)


cem = murat

cem.isim_yaz()

cem.isim = "cem"

murat.isim_yaz()

print(id(cem))

print(id(murat))

# shallow copy : instance create eder yani obje oluşturur
# ancak kopyalan objenin niteklikleri create etmez yani niteliklerin instace ını oluşturmaz. 
# halen ikiş objenin nitelikşier aynıdır.

import copy

oguz=copy.copy(murat) # shallow copy

oguz.isim_yaz()
print("-------------------------")
print(id(oguz))

print(id(murat))

print("-------------------------")

print(id(oguz.isim))

print(id(murat.isim))

oguz.isim_yaz()
murat.isim_yaz()


print("-------------------------")

oguz.isim = str("oğuz")

print(id(oguz.isim))

print(id(murat.isim))

print("-------------------------")


print(oguz.isim)
print(murat.isim)


## kopyalanan objenin içndeki bütün instance ları da kopyalar
print("###############################################")
import copy
ahmet = copy.deepcopy(murat)
print(id(murat))
print(id(ahmet))
print("---------------------------")
print(id(murat.liste))
print(id(ahmet.liste))
print("---------------------------")
print(id(murat.isim))
print(id(ahmet.isim))
print("---------------------------")
print(id(murat.liste[0]))
print(id(ahmet.liste[0]))


a = str("ahmet")
b = str("mehmet")



print(id(a))
print(id(b))



c = []
d = []


print(id(c))
print(id(d))




test = "abc"

def test_abc(metin):
    print(id(metin))
    global test
    metin = "sdfsdsdf"
    print(id(metin))
    print(id(test))
    test = "ali veli"

print("-----------------------")
print(id(test))

test_abc(test)



print(id(test))


print(test)
