from .fatura import Fatura
from . import fatura_veri_yonetimi
import re

def __fatura_dogrula(fatura: Fatura) -> (bool,str):
    pattern     = "[A-Z]{3}[2021][0-9]{10}"
    sonuc       = re.search(pattern, fatura.no)
    # pattern2    = "[0]{1}[1-9]{1}[0-9]{9}"
    # sonuc2      = re.search(pattern2, fatura.tel)
    if sonuc == None:
        return (False, "Fatura numarası uyumsuzdur!")
    
    if fatura_veri_yonetimi.fatura_getir_faturano(fatura.no) != None:
        return (False, "{fatura.tckn} Fatura numarası daha önce sisteme kaydedilmiş!")

    if fatura.tutar.isnumeric() != True:
        return (False, "Fatura tutarı rakamlardan oluşmalıdır!")

    return (True, "Fatura doğrulandı")

def fatura_ekle(fatura:Fatura) -> (bool,str):
    try:
        dogrulama_sonucu = __fatura_dogrula(fatura)

        if dogrulama_sonucu[0] == False:
            return dogrulama_sonucu
        
        fatura_veri_yonetimi.fatura_ekle(fatura)

        return (True, "Kayıt başarıyla yapılmıştır.")
    except Exception as ex:
        return (False, "Hata meydana geldi : " + ex.__str__())        

def fatura_listele() -> {Fatura}:
    return fatura_veri_yonetimi.fatura_listele()

def fatura_sil(benzersiz_kod: int) -> bool:
    try:
        fatura_veri_yonetimi.fatura_sil(benzersiz_kod)
    except:
        return False

def fatura_duzenle(fatura:Fatura) -> (bool,str):
    try:
        dogrulama_sonucu = __fatura_dogrula(fatura)

        if dogrulama_sonucu[0] == False:
            return dogrulama_sonucu

        fatura_veri_yonetimi.fatura_duzenle(fatura)[fatura.benzersiz_kod]=fatura

        return (True, "Kayıt başarıyla yapılmıştır.")
    except Exception as ex:
        return (False, "Hata meydana geldi : " + ex.__str__())
    
def arac_getir(benzersiz_kod: int) -> Fatura:
    try:
        return fatura_veri_yonetimi.fatura_getir_benzersizkod(benzersiz_kod)
    except:
        return Fatura()
