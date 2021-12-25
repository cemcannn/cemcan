from .personel import Personel
__personel_listesi=dict()

def personel_ekle(personel:Personel):
    __personel_listesi[personel.benzersiz_kod]=[personel.tckn,personel.adi,personel.soyadi,personel.adres,personel.tel,personel.gorev]

def personel_sil(benzersiz_kod:int):
    __personel_listesi.pop(benzersiz_kod)

def personel_getir_benzersizkod(benzersiz_kod:int) -> Personel: 
    return __personel_listesi[benzersiz_kod] 

def personel_getir_tckn(tckn:int):
    for personel in __personel_listesi.items():
        if personel[0] == tckn:
            return personel
    return None

def personel_listele() -> Personel:
    return __personel_listesi

def personel_duzenle(personel:Personel):
    __personel_listesi[personel.benzersiz_kod] = personel