from .musteri import Musteri
__musteri_listesi=dict()

def musteri_ekle(musteri:Musteri):
    __musteri_listesi[musteri.benzersiz_kod]=musteri

def musteri_sil(benzersiz_kod:int):
    __musteri_listesi.pop(benzersiz_kod)

def musteri_getir_benzersizkod(benzersiz_kod:int) -> Musteri: 
    return __musteri_listesi[benzersiz_kod] 

def musteri_getir_tckn(tckn:int):
    for musteri in __musteri_listesi.items():
        if musteri.tckn == tckn:
            return musteri
    return None

def musteri_listele() -> Musteri:
    return __musteri_listesi

def musteri_duzenle(musteri:Musteri):
    __musteri_listesi[musteri.benzersiz_kod] = musteri