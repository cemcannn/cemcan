

from muratin_hesap_makinasi import HesapMakinasi

sayi1 = 3
sayi2 = 2


hesap_makinasi = HesapMakinasi()

sonuc = hesap_makinasi.topla(sayi1, sayi2)
if sonuc != 5:
    raise Exception("Sonuc 5 olmalıydı")

sonuc = hesap_makinasi.cikart(sayi1, sayi2)
if sonuc != 1:
    raise Exception("Sonuc 1 olmalıydı")

sonuc = hesap_makinasi.bol(sayi1, sayi2)
if sonuc != 1.5:
    raise Exception("Sonuc 1.5 olmalıydı")

sonuc = hesap_makinasi.carp(sayi1, sayi2)
if sonuc != 6:
    raise Exception("Sonuc 6 olmalıydı")

print("herşey yolunda")


