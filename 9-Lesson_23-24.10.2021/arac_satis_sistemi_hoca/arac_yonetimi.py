
class Arac:
    def __init__(self):
        self.marka  = ""
        self.model  = ""
        self.renk   = ""
        self.hiz    = 0
        self.id     = ""
        self.km     = 0
    
    def calistir(self):
        print(f"{self.id} seri numaralı araç çalıştı")
    
    def durdur(self):
        print(f"{self.id} seri numaralı araç durduruldu")
    
    def git(self, km:int):
        print(f"{self.id} seri numaralı araç hareket etti")
        self.km = self.km + km
    def gittigi_km_sayacini_yazdir(self):
        print(str(self.km))
