from typing import Callable


class StandardMatematik:
    def toplama(sayi1:int, sayi2:int) -> int:
        return sayi1 + sayi2

    def cikarma(sayi1:int, sayi2:int) -> int:
        return sayi1 - sayi2

    def carpma(sayi1:int, sayi2:int) -> int:
        return sayi1 * sayi2

    def bolme(sayi1:int, sayi2:int) -> int:
        return sayi1 / sayi2

class BilimselMatematik:
    def ussu_alma(sayi1_taban:int, sayi2_us:int) ->int :
        return sayi1_taban ** sayi2_us

    def kare_al(sayi:int) -> int:
        return sayi ** 2

def modul_adi_yaz(modul_adi:Callable):
    pass