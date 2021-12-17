from .musteri import Musteri
from . import musteri_veri_yonetimi
import re

def __musteri_dogrula(musteri: Musteri) -> (bool,str):
    pattern = "[1-9]{1}[0-9]{10}"
    sonuc   = re.search(pattern, musteri.tckn)
    if sonuc == None:
        return (False, "TCKN 11 Haneli olmalıdır!")

    # if sonuc == "[0]{1}[0-9]{10}":
    #     return (False, "TCKN '0' ile başlayamaz!")
    
    if musteri_veri_yonetimi.musteri_getir_tckn(musteri.tckn) != None:
        return (False, "{musteri.tckn} TCKN'ye müşteri daha önce sisteme kaydedilmiş!")
    
    if type(musteri.tckn) != int:
        return (False, "TCKN rakamlardan oluşmalıdır!")

def musteri_ekle(musteri:Musteri) -> (bool,str):
    try:
        dogrulama_sonucu = __musteri_dogrula(musteri)
        if dogrulama_sonucu[0] == False:
            return dogrulama_sonucu
        
        musteri_veri_yonetimi.musteri_ekle(musteri)

        return (True, "Kayıt başarıyla yapılmıştır.")
    except Exception as ex:
        return (False, "Hata meydana geldi : " + ex.__str__())        

def musteri_listele() -> {Musteri}:
    return musteri_veri_yonetimi.musteri_listele()

def musteri_sil(tckn: int) -> bool:
    try:
        musteri_veri_yonetimi.musteri_sil(tckn)
    except:
        return False

def musteri_duzenle(musteri:Musteri) -> (bool,str):
    try:
        dogrulama_sonucu = __musteri_dogrula(musteri)

        if dogrulama_sonucu[0] == False:
            return dogrulama_sonucu

        musteri_veri_yonetimi.musteri_duzenle(musteri)[musteri.tckn]=musteri

        return (True, "Kayıt başarıyla yapılmıştır.")
    except Exception as ex:
        return (False, "Hata meydana geldi : " + ex.__str__())
    
def arac_getir(tckn: int) -> Musteri:
    try:
        return musteri_veri_yonetimi.musteri_getir_tckn(tckn)
    except:
        return Musteri()
