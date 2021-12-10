# class A:
#     pass

# class B:
#     def __init__(self):
#         self.A=""
#         self.isim=""

# a=A()
# b=B()

# b.A=a

# def b_ye_isim_ata(isim):
#     if isim.isnumeric():
#         raise Exception("isim rakam olamaz")

#     if len(isim)<3:
#         raise Exception("isim parametresinin karakter sayısı 3'den küçük")
#         b.isim=isim

# b_ye_isim_ata("Cem")
# # Class ın kendisiyle ilgili olan konuları kendi içinde çözmemiz gerekir.
# # Ancak B'nin ismine atama yaparken gerekli olan doğrulamaları üstte b 
# # Aslında B classı içinde halletmemiz lazım.
# print(b.isim)

class A:
    pass

class B:
    def __init__(self, isim:str,a:A):
        if isim.isnumeric():
            raise Exception("isim rakam olamaz")

        if len(isim)<3:
            raise Exception("isim parametresinin karakter sayısı 3'den küçük")
            b.isim=isim

        self.isim   = ""
        self.a      = ""

a = A
b = B("cem",a)
