class Arac: # Araç kodu
    def __init__(self, benzersiz_kod: int, serino: str, marka: str, model: str, fiyat: int, renk: str):
        self.benzersiz_kod  = benzersiz_kod
        self.serino         = serino # pattern A000-0000
        self.marka          = marka
        self.model          = model
        self.fiyat          = fiyat
        self.renk           = renk

    def __str__(self): # Bu ne işe yarıyor.##############################################
        return f"ID = {self.benzersiz_kod}, serino = {self.serino}, marka = {self.marka}, model = {self.model}"

