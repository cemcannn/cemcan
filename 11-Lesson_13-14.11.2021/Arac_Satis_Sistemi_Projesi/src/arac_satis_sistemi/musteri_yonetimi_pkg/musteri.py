class Musteri:
    def __init__(self,tckn:int,adi:str,soyadi:str,adres:complex,tel:int):
        self.tckn   = tckn
        self.adi    = adi
        self.soyadi = soyadi
        self.adres  = adres
        self.tel    = tel

    def __str__(self): 
        return f"TCKN = {self.tckn}, Ad = {self.adi}, Soyad = {self.soyadi}, Adres = {self.adres}, Telefon = {self.tel} "
