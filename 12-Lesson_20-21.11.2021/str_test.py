class Insan:
    def __init__(self,isim:str, dogum_yili:int):
        self.isim=isim
        self.dogum_yili=dogum_yili

    def __str__(self):
        return f"adı : {self.isim}, doğum yılı : {self.dogum_yili}"

murat = Insan("murat",1980)

print(murat.isim, murat.dogum_yili)

print(murat)