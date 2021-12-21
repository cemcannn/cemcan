from .fatura import Fatura
from . import fatura_veri_yonetimi
from . import fatura_menu_yonetimi as fmy
import re

# Motor silindir hacmi 1600 cm³’ü geçmeyen, matrahı 92 bin TL’ye kadar olan araçların ÖTV oranı %45
# Motor silindir hacmi 1600 cm³’ü geçmeyen, matrahı 92 bin TL ile 150 bin TL arası araçların ÖTV oranı %50
# Motor silindir hacmi 1600 cm³’ü geçmeyen, matrahı 150 bin TL üzeri araçların ÖTV oranı %80
# Motor silindir hacmi 1600 cm³ ile 2000 cm³ arası, matrahı 170 bin TL’ye kadar araçların ÖTV oranı %130
# Motor silindir hacmi 1600 cm³ ile 2000 cm³ arası, matrahı 170 bin TL üzeri araçların ÖTV oranı %150
# 2000 cm³ üzeri motor silindir hacmi olan matrahında sınır olmayan araçların ÖTV oranı %220

def __vergi_hesapla(fatura_arac: int) -> (int):
    if fatura_arac[5] <= 1599 and fatura_arac[3] <= 91000:
        fatura_tutar = fatura_arac[3] * 0,45 * 0,18  
        return fatura_tutar
    elif fatura_arac[5] <= 1599 and fatura_arac[3] >= 92000 and fatura_arac[3] <= 149000:
        fatura_tutar = fatura_arac[3] * 0,50 * 0,18  
        return fatura_tutar
    elif fatura_arac[5] <= 1599 and fatura_arac[3] >= 150000:
        fatura_tutar = fatura_arac[3] * 0,80 * 0,18  
        return fatura_tutar      
    elif fatura_arac[5] >= 1600 and fatura_arac[5] <= 1999 and fatura_arac[3] <= 169000:
        fatura_tutar = fatura_arac[3] * 1,30 * 0,18  
        return fatura_tutar
    elif fatura_arac[5] >= 1600 and fatura_arac[5] <= 1999 and fatura_arac[3] >= 170000:
        fatura_tutar = fatura_arac[3] * 1,50 * 0,18  
        return fatura_tutar
    elif fatura_arac[5] >= 2000:
        fatura_tutar = fatura_arac[3] * 2,20 * 0,18  
        return fatura_tutar

def __fatura_dogrula(fatura: Fatura) -> (bool,str):
    pattern     = "[A-Z]{3}[2021][0-9]{6}"
    sonuc       = re.search(pattern, fatura.no)
    # pattern2    = "[0]{1}[1-9]{1}[0-9]{9}"
    # sonuc2      = re.search(pattern2, fatura.tel)
    if sonuc == None:
        return (False, "Fatura numarası AAA2021000001 patternine uymalıdır!")
    
    if fatura_veri_yonetimi.fatura_getir_faturano(fatura.no) != None:
        return (False, "{fatura.no} Fatura numarası daha önce sisteme kaydedilmiş!")

    # if type(fatura.tutar) != int:
    #     return (False, "Fatura tutarı rakamlardan oluşmalıdır!")

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
