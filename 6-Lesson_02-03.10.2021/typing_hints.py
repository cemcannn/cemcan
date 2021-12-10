
# def hesapla(degisken):
#     """değişken : int"""
#     print(degisken + 1)
#     return 5

# hesapla() # ide burada değişken parametresi hakkında bilgi veremez.

# def give_msg(name):
#     print(name)

# give_msg("cem")

# # Üsttekinin typing ile yazılması

# def mesaj_ver(isim:str, kac_kere:int):
#     for i in list(range(1, kac_kere+1)):
#         print(f"merhaba eeey {isim}")

# mesaj_ver("Selim",2)

# def mesaj_ver(isim:str, kac_kere:int) -> str:
#     for i in list(range(1, kac_kere+1)):
#         print(f"merhaba eeey {isim}")
#     return "mesajlar verildi"

# mesaj = mesaj_ver("Selim",2)

# print(mesaj)

# #listelerde çalışmak

# def mesaj_ver(isim_listesi:list[str]) -> str:
#     for isim in isim_listesi:
#         print(f"merhaba eeey {isim}")
#     return "mesajlar verildi"

# mesaj = mesaj_ver(["Murat","Selim","Tuğçe"])

# print(mesaj)

# Fonksiyon parametre hint kullanımı
# isim="ahmet"

# from typing import Callable

# def mesaji_cagir(fonksiyon:Callable[[str],str]) -> str:
#     sonuc = fonksiyon(isim)
#     print(sonuc)
#     return "mesaj verildi"

# def mesaj_ver(isim) -> str:
#     print("merhaba", isim)
#     return "mesaj ver çalıştı"

# mesaj=mesaji_cagir(mesaj_ver)
# print(mesaj)

