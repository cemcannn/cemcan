from arac_yonetimi_pkg import arac
from musteri_yonetimi_pkg import musteri

class Fatura:
    def __init__(self,benzersiz_kod: int, no:int, arac: arac.Arac, musteri: musteri.Musteri, tutar:int):
        self.benzersiz_kod  = benzersiz_kod
        self.no             = no    
        self.arac           = arac
        self.musteri        = musteri
        self.tutar          = tutar

    def __str__(self): 
        return f"ID = {self.benzersiz_kod}, Fatura No = {self.no}, Araç = {self.arac}, Müşteri = {self.musteri}, Fatura Tutarı = {self.tutar} "
