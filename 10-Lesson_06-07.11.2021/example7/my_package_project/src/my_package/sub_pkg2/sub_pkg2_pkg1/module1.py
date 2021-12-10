__all__ = ["fonksiyon","Module1Class1"]




def fonksiyon():
    print ("ben modul1")


class Module1Class1:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "sub_pkg2 atında sub_pkg1_pkg1 altında Module1 altındaki Module1Class1 classıyım. Runtime Adım:" + __name__
    
    def name_getir(self):
        return self.name

print(__name__ + " yüklendi")
