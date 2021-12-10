

def faktoriyel(sayi):
    liste=1
    for i in list(reversed(range(1,int(sayi)+1))):
        liste = liste * i
    print("Faktöriyel sonucu :",liste)


while True:
    rakam=input("Rakam giriniz : ")
    if rakam.isnumeric() == True:
        faktoriyel(rakam)
    else:
        print("Lütfen rakam giriniz.")

    secenek=input("""devam için "e", çıkmak için "h"ye basınız.""")
    if secenek == "h":
        break

