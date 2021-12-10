# testden rakam üretecek bir object. yani range fonksiyonun tersini istiyoruz
# son rakamda None yazacak

class Sayilar:

    def __init__(self, sayi: int):
        self.a = sayi
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        x = self.a
        self.a -= 1
        if self.a >= 0:
            return x
        else:
            self.b += 1
            if self.b < 11:
                return None
            else:
                raise StopIteration


sayilar = Sayilar(5)
sayilar_iter = iter(sayilar)

for i in sayilar_iter:
    if i != None:
        print(i)
    else:
        break

