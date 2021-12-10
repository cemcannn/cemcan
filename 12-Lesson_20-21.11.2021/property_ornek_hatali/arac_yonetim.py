from arac import Arac




def arac_ekle():

    arac=Arac(1,"1","ford","focus",1,"kırmızı")

def arac_duzenle():
    arac= Arac.arac_bul("ford")

    # bu  aslında bir property ve setter olarak yazılmalıydı
    #arac.model = "fiat"
    arac.model_degistir("fiat")

    Arac.arac_degistir(arac)


    # bu  aslında bir property ve setter olarak yazılmalıydı
    #arac_model = arac.model
    arac_model = arac.model_getir()

    print(arac_model)



