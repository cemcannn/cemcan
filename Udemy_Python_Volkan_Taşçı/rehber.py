rehber = {
    "kisi": {
    "ev adresi": "Bostan sokak no 12",
    "iş adresi": "Karamel sokak no 13",
    "ev telefonu": "5302555555",
    }
}

isimler = rehber.keys()

arananKisi = input("Aranan isim : ")

if arananKisi in isimler:
    flag = True

else: 
    flag = False

arananOzellik = input("Aranan özellik : ")

if flag:
    print(rehber.get(arananKisi).get(arananOzellik,"Aranan özellik bulunamadı!"))

else:
    print("Aranan kişi bulunamadı!")