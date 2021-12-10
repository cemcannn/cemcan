class Insan: # base class - alt sınıf
    def __init__(self,isim:str, boy:float, kilo:int):
        self.isim= isim
        self.boy=boy
        self.kilo = kilo
    
    def yuru(self, adim_sayisi:int):
        print(adim_sayisi + " adım atıldı")
 
    def uyu(self):
        print("uyudu")  
 
    def boy_yazdir(self):
        print(self.boy)
 
class Muhendis(Insan): # "İnsan" sınıfı alt-sınıfı, aynı zamanda "Bilgisayar Mühendisi" sınıfının üst-sınıfıdır.
    def __init__(self, isim: str, boy: float, kilo: int, dogum_yili:int):
        super().__init__(isim, boy, kilo)
        self.dogum_yili=dogum_yili
    
    def toplaya_katil(self):
        print("toplantıya katıldı")
    
    def hesap_yap(self):
        print("ilk hesap yapıldı")
 
    def dogum_yili_yazdir(self):
        print(self.dogum_yili)
 
class BilgisayarMuhendisi(Muhendis):
    def kod_yaz(self):
        print("kod yazıldı")
 
class InsaatMuhendisi(Muhendis):
    def __init__(self, diploma_verilis_yili:int):
        self.diplama_verilis_yili=diploma_verilis_yili
 
    def diploma_yil_yazdir(self):
        print(self.diplama_verilis_yili)
 
    def cizim_yap(self):
        print("çizim yapıldı") 
 
insaat_muhendisi_omer = InsaatMuhendisi(2000)
 
insaat_muhendisi_omer.diploma_yil_yazdir()
 
#print(insaat_muhendisi_omer.isim)
 
# üstteki iş,imizi görmedi o yüzden alttakini yazdık
 
class InsaatMuhendisi2(Muhendis):
    def __init__(self, isim: str, boy: float, kilo: int, diploma_verilis_yili:int):
        self.diplama_verilis_yili=diploma_verilis_yili
 
    def diploma_yil_yazdir(self):
        print(self.diplama_verilis_yili)
 
    def cizim_yap(self):
        print("çizim yapıldı") 
 
insaat_muhendisi_omer2 = InsaatMuhendisi2("ömer",1.80,80,2000)
insaat_muhendisi_omer2.diploma_yil_yazdir()
 
#print(insaat_muhendisi_omer2.isim)
 
# Ancak bu da işimiz görmedi çünkü halen 
# Insan classındaki __init__ fonskiyonundaki tanımlamalara ulaşamıyoruz
# Bu nedenlata alttaki class ı yazdık
 
class InsaatMuhendisi3(Muhendis):
    def __init__(self, isim: str, boy: float, kilo: int, diploma_verilis_yili:int, dogum_yili:int):
        super().__init__(isim,boy,kilo,dogum_yili)
        self.diplama_verilis_yili=diploma_verilis_yili
 
    def diploma_yil_yazdir(self):
        print(self.diplama_verilis_yili)
 
    def cizim_yap(self):
        print("çizim yapıldı") 
 
insaat_muhendisi_omer3 = InsaatMuhendisi3("ömer",1.80,80,2000,1980)
insaat_muhendisi_omer3.diploma_yil_yazdir()
print(insaat_muhendisi_omer3.isim)
insaat_muhendisi_omer3.boy_yazdir()
insaat_muhendisi_omer3.dogum_yili_yazdir()
 
## eğer alt sınıfla ilgili hiçbir nitelik, fonksiyon veya 
#  __init__ fonksiyonu ezilmediyse alttaki gibi kullanılabilir
 
class InsaatMuhendisi4(Muhendis):
    def hesap_yap(self):
        print("yeni hesap yapıldı")
        super().hesap_yap()
        super().toplaya_katil()
        
 
insaat_muhendisi_omer4 = InsaatMuhendisi4("omer",1.8,78,1980)
insaat_muhendisi_omer4.boy_yazdir() # insan classından kullanık
insaat_muhendisi_omer4.dogum_yili_yazdir() # muhensin
 
insaat_muhendisi_omer4.hesap_yap()
 
# 4 polymorphism (çok biçimlilik)
# inherit edilen class ı farklılaştırmak 
# Bir classın birden farklı şekilde davranabilmesi
# inheritance maddesinde bunu bol bol yaptık
# Mesela inşaat mühendisliği class ını farklı formasyonlara sokuyoruz