############################# iterator ###############################
# 1. iteration: objeleri sırasıyla dolaşma işlemidir
# 2. iterable: iterasyon işlemine tabi tutulabilen objedir.
# 3. iterator: iterable objeleri iterator işlemine tutmamızı sağlayan objelerdir.

# iterable bir obje oluşturmak için objenin iki fonksiyona sahip olması gerekir.

# __iter__
# __next__

liste = [1,2,3,4,5,6]
iterable = iter(liste)

print(next(iterable))
# sonuc : 1
print(next(iterable))
# sonuc : 2


# kendi iterable objemizi nasıl yazarız

class Sayilar:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

sayilar = Sayilar()
sayilar_iter = iter(sayilar)
print(next(sayilar_iter))
print(next(sayilar_iter))
print(next(sayilar_iter))
print(next(sayilar_iter))
print(next(sayilar_iter))
print(next(sayilar_iter))
print(next(sayilar_iter))
print(next(sayilar_iter))

for i in sayilar:
    if i < 20:
        print(i)
    else:
        break


for i in sayilar_iter:
    if i < 20:
        print(i)
    else:
        break

print(sayilar)
print(Sayilar)

print(type(sayilar))
print(type(sayilar_iter))


class SayilarSonlu:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        if self.a < 10:
            return x
        else:
            raise StopIteration


sayilar_sonlu = SayilarSonlu()
sayilar_sonlu_iter = iter(sayilar_sonlu)

for i in range(15):
    print(next(sayilar_sonlu_iter))






