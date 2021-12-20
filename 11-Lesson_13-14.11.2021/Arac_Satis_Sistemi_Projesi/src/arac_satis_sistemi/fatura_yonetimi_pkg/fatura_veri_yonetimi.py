from .fatura import Fatura
__fatura_listesi=dict()

def fatura_ekle(fatura:Fatura):
    __fatura_listesi[fatura.benzersiz_kod]=fatura

def fatura_sil(benzersiz_kod:int):
    __fatura_listesi.pop(benzersiz_kod)

def fatura_getir_benzersizkod(benzersiz_kod:int) -> Fatura: 
    return __fatura_listesi[benzersiz_kod] 

def fatura_getir_faturano(tckn:int):
    for fatura in __fatura_listesi.items():
        if fatura.tckn == tckn:
            return fatura
    return None

def fatura_listele() -> Fatura:
    return __fatura_listesi

def fatura_duzenle(fatura:Fatura):
    __fatura_listesi[fatura.benzersiz_kod] = fatura