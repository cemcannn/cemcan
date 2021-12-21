from .musteri import Musteri
__musteri_listesi={4565:[32271333288,"CEM","CAN","AHİ MESUT",5557863544]}

def musteri_ekle(musteri:Musteri):
    __musteri_listesi[musteri.benzersiz_kod]=[musteri.tckn,musteri.adi,musteri.soyadi,musteri.adres,musteri.tel]

def musteri_sil(benzersiz_kod:int):
    __musteri_listesi.pop(benzersiz_kod)

def musteri_getir_benzersizkod(benzersiz_kod:int) -> Musteri: 
    return __musteri_listesi[benzersiz_kod] 

def musteri_getir_tckn(tckn:int):
    for musteri in __musteri_listesi.items():
        if musteri[0] == tckn:
            return musteri
    return None

def musteri_listele() -> Musteri:
    return __musteri_listesi

def musteri_duzenle(musteri:Musteri):
    __musteri_listesi[musteri.benzersiz_kod] = musteri