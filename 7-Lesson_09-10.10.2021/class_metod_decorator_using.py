class Insan:
    class_isimler = []
    def __init__(self):
        self.isim=""
    
    def isim_ver(self, isim):
        self.isim = isim
        self.class_isimler.append(isim)
    
    
    @classmethod
    def isimleri_getir(cls):
        return cls.class_isimler




i1 = Insan()
i1.isim_ver("Murat")

i2=Insan()
i2.isim_ver("Görkem")

i3=Insan()
i3.isim_ver("Cem")

print(str(len(Insan.isimleri_getir())))



