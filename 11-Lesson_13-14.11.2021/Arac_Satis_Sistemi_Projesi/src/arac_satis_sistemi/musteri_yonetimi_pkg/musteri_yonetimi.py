from .musteri import Musteri
from . import musteri_veri_yonetimi
import re

def __musteri_dogrula(musteri: Musteri) -> (bool,str):
    pattern     = "[1-9]{1}[0-9]{10}"
    sonuc       = re.search(pattern, musteri.tckn)
    pattern2    = "[1-9]{1}[0-9]{9}"
    sonuc2      = re.search(pattern2, musteri.tel)
    if sonuc == None:
        return (False, "TCKN 11 Haneli Olmalıdır!")

    if sonuc == "[0]{1}[0-9]{10}":
        return (False, "TCKN '0' ile Başlayamaz!")
    
    if musteri_veri_yonetimi.musteri_getir_tckn(musteri.tckn) != None:
        return (False, "{musteri.tckn} İlgili Müşteri TCKN Daha Önce Sisteme Kaydedilmiş!")
    
    if musteri.tckn.isnumeric() != True:
        return (False, "TCKN Rakamlardan Oluşmalıdır!")
    
    if sonuc2 == None:
        return (False, "Lütfen Telefon Numarasını Doğru Giriniz!")

    if musteri.tel.isnumeric() != True:
        return (False, "Telefon Numarası Rakamlardan Oluşmalıdır!")

    return (True, "Müşteri Doğrulandı")

def musteri_ekle(musteri:Musteri) -> (bool,str):
    try:
        dogrulama_sonucu = __musteri_dogrula(musteri)

        if dogrulama_sonucu[0] == False:
            return dogrulama_sonucu
        
        musteri_veri_yonetimi.musteri_ekle(musteri)

        return (True, "Kayıt Başarıyla Yapılmıştır.")
    except Exception as ex:
        return (False, "Hata Meydana Geldi : " + ex.__str__())        

def musteri_listele() -> {Musteri}:
    return musteri_veri_yonetimi.musteri_listele()

def musteri_sil(benzersiz_kod: int) -> bool:
    try:
        musteri_veri_yonetimi.musteri_sil(benzersiz_kod)
    except:
        return False

def musteri_duzenle(musteri:Musteri) -> (bool,str):
    try:
        dogrulama_sonucu = __musteri_dogrula(musteri)

        if dogrulama_sonucu[0] == False:
            return dogrulama_sonucu

        musteri_veri_yonetimi.musteri_duzenle(musteri)[musteri.benzersiz_kod]=musteri

        return (True, "Kayıt Başarıyla Yapılmıştır.")
    except Exception as ex:
        return (False, "Hata Meydana Geldi : " + ex.__str__())
    
def arac_getir(benzersiz_kod: int) -> Musteri:
    try:
        return musteri_veri_yonetimi.musteri_getir_benzersizkod(benzersiz_kod)
    except:
        return Musteri()
