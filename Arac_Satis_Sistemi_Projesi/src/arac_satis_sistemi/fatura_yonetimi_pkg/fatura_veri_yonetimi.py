from .fatura import Fatura
__fatura_listesi=dict()

def fatura_ekle(fatura:Fatura):
    __fatura_listesi[fatura.benzersiz_kod]=[fatura.no,fatura.arac,fatura.musteri,fatura.personel,fatura.tutar,fatura.tarih]

def fatura_sil(benzersiz_kod:int):
    __fatura_listesi.pop(benzersiz_kod)

def fatura_getir_benzersizkod(benzersiz_kod:int) -> Fatura: 
    return __fatura_listesi[benzersiz_kod] 

def fatura_getir_faturano(no:complex):
    for fatura in __fatura_listesi.items():
        if fatura[0] == no:
            return fatura
    return None

def fatura_listele() -> Fatura:
    return __fatura_listesi

def fatura_duzenle(fatura:Fatura):
    __fatura_listesi[fatura.benzersiz_kod] = fatura