def topla(birinci_sayi, ikinci_sayi):
    sonuc = birinci_sayi + ikinci_sayi
    print(sonuc)

# ya da 
def topla(birinci_sayi, ikinci_sayi):
    sonuc = birinci_sayi + ikinci_sayi
    return sonuc


#Üçgen kontrol uygulaması
def ucgen_mi(a,b,c):
    if a**2+b**2==c**2:
        return "Girdiğiniz değerler üçgendir."
    else:
        return "Girdiğiniz değerler üçgen değildir."

print(ucgen_mi(3,4,5))

