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

def modul_adi_yaz():
    print("Matematik Modülü")

if __name__=="__main__": # Bu dosya normalde if bloğunu eklemeseydik, bu dosyayı import ettiğimizde aşağıdaki print ile nereden import edildiğini yazacaktı fakat if bloğu ile sadece ana dosya olarak direkt çalıştııldığında kullanılmasını sağladık.
    print ("Ben matematik modülü.py dosyasıyım, adım: ", __name__)
    print ("----------------------------------------------------")