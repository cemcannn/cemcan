from arac_yonetimi_pkg import arac_menu_yonetimi #araç yönetimi paket dosyasından araç menu yönetimi  dosyası çekiliyor
from musteri_yonetimi_pkg import musteri_menu_yonetimi 
from personel_yonetimi_pkg import personel_menu_yonetimi 
from fatura_yonetimi_pkg import fatura_menu_yonetimi 


menu_metni = """ Seçenekler:
                [1] Araç Yönetimi İçin 
                [2] Müşteri Yönetimi İçin 
                [3] Personel Yönetimi İçin 
                [4] Fatura Yönetimi İçin 
                [5] Çıkmak İçin 5"""


def ana_menu_getir(): 
    while True:
        print(menu_metni)
        secenek = int(input("menu seçinizi yapınız: "))
        if secenek == 1:
            arac_menu_yonetimi.menu_getir()
        elif secenek == 2:
            musteri_menu_yonetimi.menu_getir()
        elif secenek == 3:
            personel_menu_yonetimi.menu_getir()
        elif secenek == 4:
            fatura_menu_yonetimi.menu_getir()
        elif secenek == 5:
            quit()
        else:
            print("yanlış seçim yaptınız")