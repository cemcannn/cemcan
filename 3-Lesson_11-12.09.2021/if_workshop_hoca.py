sayi1 = input("sayı1 giriniz: ")
sayi2 = input("sayı2 giriniz: ")


durum = True

if sayi1.isnumeric() == True:
    sayi1 = int(sayi1)
    durum = True
else:
    print("sayı1 değişkenini numerik girmediniz.")
    durum = False

if sayi2.isnumeric() == True and durum == True:
    sayi2 = int(sayi2)
    durum = True
else:
    print("sayı2 değişkenini numerik girmediniz.")
    durum = False



if durum==True:
    
    secenek = input("""Seçenekler: 
                    \n - Toplama(+) 
                    \n - Çıkartma(-) 
                    \n - Çarpma(*)  
                    \n - Bölme(/)                     
                    \n Yapmak istediğiniz işlerimi seçiniz: """)

    if secenek == "+":
        print("toplama işlemi sonucu: {}".format(sayi1 + sayi2))
    elif secenek == "-":
        print("çıkartma işlemi sonucu: {}".format(sayi1 - sayi2))
    elif secenek == "*":
        print("çarpma işlemi sonucu: {}".format(sayi1 * sayi2))
    elif secenek == "/":
        print("bölme işlemi sonucu: {}".format(sayi1 / sayi2))

    else:
        print("lütfen doğru işlemi seçiniz")
else:
    pass

