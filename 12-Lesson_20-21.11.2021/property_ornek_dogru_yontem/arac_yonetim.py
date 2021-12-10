from arac import Arac




def arac_ekle():

    arac=Arac(1,"1","ford","focus",1,"kırmızı")

def arac_duzenle():
    arac= Arac.arac_bul("ford")

    arac.model = "fiat"

    Arac.arac_degistir(arac)

    print (arac.tramer)

    arac_model = arac.model

    print(arac_model)



