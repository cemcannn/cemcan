from .arac import Arac # arac modülünden Arac class ını import ediyoruz.
__arac_listesi=dict() # __arac_listesi değişkenine bir sözlük atayıp gizliyoruz.

def arac_ekle(arac:Arac): # Arac ekle fonksiyonu keyword arguments olarak arac parametresi Araç classı olarak tanımlanıyor.
    __arac_listesi[arac.benzersiz_kod]=[arac.serino,arac.marka,arac.model,arac.fiyat,arac.renk] # arac listesinin arac benzersiz kod indeksi arac parametresine eşitleniyor yani key olarak arac benzersiz kod value değerleri ise arac class ının geri kalan parametreleri oluyor.

def arac_sil(benzersiz_kod:int):
    __arac_listesi.pop(benzersiz_kod) # araç listesinden pop fonksiyonu ile benzersiz kod key ini girince ilgili araç class ını siliyor.

def arac_getir_benzersizkod(benzersiz_kod:int) -> Arac: # Araç getir fonksiyonunu benzersiz koddan çağırıyor.
    return __arac_listesi[benzersiz_kod] # 

def arac_getir_serino(serino:str) -> Arac: # Araç getir fonksiyonunu seri numaradan getiriyor.
    for arac in __arac_listesi.items():
        if arac.serino == serino:
            return arac
    return None

def arac_listele() -> {Arac}: #Burası neden süslü parantez#################################### 
    return __arac_listesi

def arac_duzenle(arac:Arac):
    __arac_listesi[arac.benzersiz_kod]=arac