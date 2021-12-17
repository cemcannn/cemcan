from .musteri import Musteri
__musteri_listesi=dict()

def musteri_ekle(musteri:Musteri):
    __musteri_listesi[musteri.tckn]=musteri

def musteri_sil(tckn:int):
    __musteri_listesi.pop(tckn)

def musteri_getir_tckn(tckn:int):
    return __musteri_listesi[tckn]

def musteri_listele() -> Musteri:
    return __musteri_listesi

def musteri_duzenle(musteri:Musteri):
    __musteri_listesi[musteri.tckn] = musteri