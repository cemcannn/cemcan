class Insan:
    pass

def insan_yaz(insan:Insan):
    print(insan)

insan_yaz(Insan())

# abstract class tanımında doğrudan class ın kendisiyle değilclass ın yapısıyla ilgileniyoruz.

from abc import ABC, abstractmethod

class Insan(ABC):
    @abstractmethod
    def yuru(self, adim_sayisi:int) -> str: pass

    @abstractmethod
    def uyu(self): pass

class BenimProgramim():
    def __init__(self, insan:Insan) -> None:
        self.insan = insan

    def insan_yuru(self,adim_sayisi:int):
        print(self.insan.yuru(adim_sayisi))

    def insan_uyu(self):
        self.insan.uyu()

# insan = Insan() # Burada bu şekilde örneklendirme yapamayız, çünkü ABC class ı bu şekilde yapmamıza izin vermez, kendi class ımızı kendimiz oluşturmalıyız.

# benim_programim = BenimProgramim(insan)

# İnsan abstract classının concrete (gerçek, somut) hali
class CemInsan(Insan):
    def __init__(self): 
        pass

    def yuru(self,adim_sayisi:int) -> str:
        return str(adim_sayisi) + "adım atıldı"

    def uyu(self):
        print("uyudu")

insan = CemInsan()
benim_programim = BenimProgramim(insan)
benim_programim.insan_yuru(15)