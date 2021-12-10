# 1 Soyutlama (Abstraction)
 
## __ private (tam gizli)
 
## _ yarı gizleme
 
class Insan:
    def __init__(self, isim:str, dogum_yili:int):
        self.isim = isim
 
        self._dogum_yili = dogum_yili
        self.hobisi = ""
 
    def detaylari_goster(self):
        yas = self.__yas_hesapla()
        print(self.isim, yas)
 
    def __yas_hesapla(self) -> int:
        return self.__aktif_yil_getir() - self._dogum_yili
    
    def __aktif_yil_getir(self):
        from datetime import datetime 
        yil = datetime.now().year
        return  yil


 
murat = Insan("murat",1980)
murat.detaylari_goster()
 
ahmet = Insan("ahmet",1975)
ahmet.detaylari_goster()
ahmet.hobisi = "futbol"
 
# aslında pythonda gizli hiçbirşey yoktur. __ işareti ile sadece 
# pythona ilgili objenin (nitelik veya fonksiyon) nun gizlenmesi gerektiğini belirtiyoruz.
# python nu işareti gordüğü objeyi bulanıklaştıryor (mangling)
 
print(dir(murat))
 
print(murat._Insan__aktif_yil_getir())
 
ahmet._dogum_yili = 1965
ahmet.detaylari_goster()


 
# 2 Encapsulation (Kapsülleme/Sarmallama)

class Insan:
    def __init__(self, isim:str, dogum_yili:int):
        self.isim = isim
        self._dogum_yili = dogum_yili
        self.__yas=0

    def detaylari_goster(self):
        self.__yas_hesapla()
        print(self.isim, self.__yas)

    def __yas_hesapla(self):
        self.__yas = 2021 - self._dogum_yili

selim = Insan("Selim",1987)
selim.detaylari_goster()
selim.__yas=int(45)

print(dir(selim))
print(selim.__yas) # önüne iki underscore koyarsak gizler, gizlemeyi de önüne "_Insan" koyarak yapar. Fakat sonradan tanımladığımız "selim.__yas=int(45)" olarak tanımladığımız değer yeni tanımlandığı için okunabiliyor zaten bu da yeni bir değer olarak selim class'ının içinde ayrı bir yer alıyor.

# 3