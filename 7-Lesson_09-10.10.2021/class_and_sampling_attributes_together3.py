# bir class yazacağız aynı anda hem class 
# atttribute leri hem de orneklem attribute leri olacak
# ancak bu sefer class atribute lerini orneklem metodları içinde çağıracağız
# fakat bu sefer self objesi üzerinden çağıracağız



class Insan:
    test_niteligi = "test değeri"
    test_niteligi2=[]

    def __init__(self):
        self.isim=""
        self.boy=""
        self.hobiler=[]


    def test_nitelik_degistir(self):
        print(self.test_niteligi)

    def test_nitelik2_degistir(self):
        self.test_niteligi2.append("a")
        print(self.test_niteligi2)

i1 = Insan()
i1.test_nitelik_degistir()
i1.test_nitelik2_degistir()

i2 = Insan()
i2.test_nitelik2_degistir()

# sonuc : eğer init dışında bir değişken tanımlarsak (yani attribute veya nitelik) 
# ve bu niteliğe orneklem metodu içinde self objsi üzerinden erişirsek
# bu nitelikler bütün orneklemlerde (instace larda) ortak çalışan orneklem niteliği gibi davranır.


