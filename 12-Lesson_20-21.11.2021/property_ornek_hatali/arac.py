class Arac:
    __arac_kutuphanesi = dict()
    def __init__(self, benzersiz_kod: int, serino: str, marka: str, model: str, fiyat: int, renk: str):
        self.__benzersiz_kod = benzersiz_kod
        self.__serino = serino # pattern A000-0000
        self.__marka = marka
        self.__model = model
        self.__fiyat = fiyat
        self.__renk = renk
        self.__arac_kutuphanesi[benzersiz_kod]=self

    def __str__(self):
        return f"ID = {self.__benzersiz_kod}, serino = {self.__serino}, marka = {self.__marka}, model = {self.__model}"

    @classmethod
    def arac_degistir(cls,arac):
        cls.__arac_kutuphanesi[arac.benzersiz_kod] = arac

    # bu  aslında bir property ve setter olarak yazılmalıydı
    def model_degistir(self, model):
        self.__model=model

    # bu  aslında bir property ve setter olarak yazılmalıydı
    def model_getir(self):
        return self.__model






    @classmethod
    def arac_bul(cls,model:str):
        return cls.__arac_kutuphanesi[1]


