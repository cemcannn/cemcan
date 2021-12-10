from .arac import Arac # arac modülünden Arac class ını çekiyoruz.
import re # Regular expression modülünü import ediyoruz.
from . import arac_veri_yonetimi # araç veri yönetimi modülünü import ediyoruz.


def __arac_dogrula(arac:Arac) -> (bool,str): # __arac_dogrula fonksiynunu gizleyip keyword olarak araç parametresini araç class ına eşitliyoruz.

    pattern = "A[0-9]{3}-[0-9]{4}" # pattern değişkeni oluşturup 
    sonuc = re.search(pattern, arac.serino) 
    if sonuc == None:
        return (False, "Seri numarası A000-0000 patternine uymalıdır")

    if arac_veri_yonetimi.arac_getir_serino(arac.serino) != None:
        return (False, "Seri numarası daha önce kullanılmış")

    if type(arac.fiyat) != int:
        return (False, "Fiyat rakam olmalıdır")

    return (True, "Araç doğrulandı")


def arac_ekle(arac: Arac) -> (bool,str):
    # validasyon ve varsa diğer iş kuralları yazılmalı
    try:
        dogrulama_sonucu = __arac_dogrula(arac)

        if dogrulama_sonucu[0] == False:
            return  dogrulama_sonucu

        arac_veri_yonetimi.arac_ekle(arac)

        return (True, "Kayıt başarıyla yapılmıştır.")
    except Exception as ex:
        return (False, "Hata meydana geldi: " +  ex.__str__())

def arac_listele() -> {Arac}:
    return arac_veri_yonetimi.arac_listele()

def arac_sil(benzersiz_kod: int) -> bool:
    try:
        arac_veri_yonetimi.arac_sil(benzersiz_kod)
    except:
        return False

def arac_duzenle(arac: Arac) -> (bool, str):
    # validasyon ve varsa diğer iş kuralları yazılmalı
    try:

        dogrulama_sonucu = __arac_dogrula(arac)

        if dogrulama_sonucu[0] == False:
            return  dogrulama_sonucu

        arac_veri_yonetimi.arac_duzenle(arac) [arac.benzersiz_kod]=arac

        return (True, "Kayıt başarıyla yapılmıştır.")
    except Exception as ex:
        return (False, "Hata meydana geldi : " + ex.__str__())


def arac_getir(benzersiz_kod: int) -> Arac:
    try:
        return arac_veri_yonetimi.arac_getir_benzersizkod(benzersiz_kod)
    except:
        return Arac()

