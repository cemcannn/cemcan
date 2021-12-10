import os

class Musteri():
    def __init__(self,ID, PAROLA, ISIM):
        self.isim = ISIM
        self.id = ID
        self.parola = PAROLA
        self.bakiye = 0

class Banka():
    def __init__(self):
        self.musteriler =  list()

    def musteri_ol(self, ID: str, PAROLA: str, ISIM: str):
        self.musteriler.append(Musteri(ID, PAROLA, ISIM))
        print("Bankamıza hoşgeldiniz")

def main():
    os.system("cls")
    banka = Banka()
    while True:
        print("""
        [1] Banka Müşterisiyim
        [2] Banka Müşterisi Değilim
        """)

        secim = input("Seçiminiz : ")

        if secim == "1":
            ids = [i.id for i in banka.musteriler] # bu şekilde bir gösterimde olabilir.
            ID = input("ID: ")
            if ID in ids:
                for musteri in banka.musteriler:
                    if ID == musteri.id: # müşteri bulundu
                        print("Hoşgeldiniz {}".format(musteri.isim))
                        parola = input("Parolanız : ")
                        if parola == musteri.parola:
                            print("Giriş başarılı!")
                            while True:
                                os.system("cls")
                                print("""
                                [1] Bakiye Sorgula
                                [2] Para Yatır (Kendi Hesabıma)
                                [3] Para Yatır (Başkasının Hesabına)
                                [4] Para Çek 
                                [Q] Çıkış
                                """)

                                secim2 = input("Seçiminiz")

                                if secim2 == "1":
                                    print("Bakiyeniz {}".format(musteri.bakiye))
                                    input("Ana menüye dönmek için 'enter'a basın! ")

                                elif secim2 == "2":
                                    miktar = int(input("Miktar: "))
                                    onay = input("Kendi hesabınıza {} TL para yatırma işlemini onaylıyor musunuz? : E/H\n".format(miktar))
                                    if onay == "E" or onay == "e":
                                        musteri.bakiye += miktar
                                        print("Paranız Yatırıldı!")

                                    elif onay == "H" or "h":
                                        print("İşlem iptal edildi")

                                    else:
                                        print("Lütfen doğru seçenek seçiniz!")

                                elif secim2 == "3":
                                    arananID = input("Müşteri ID : ")
                                    if arananID in ids:
                                        for digerMusteri in banka.musteriler:
                                            if arananID == digerMusteri:
                                                miktar = int(input("Miktar: "))
                                                if miktar <= musteri.bakiye:
                                                    onay = input("{} adlı müşterimize {} TL para yatırma işlemini onaylıyor musunuz? : E/H\n".format(digerMusteri,miktar))
                                                    if onay == "e" or "E":
                                                        digerMusteri.bakiye += miktar
                                                        musteri.bakiye -= miktar

                                                    elif onay == "h" or onay == "H":
                                                        print("İşlem iptal edildi")
                                                        input("Ana menüye dönmek için 'enter'a basınız! ")

                                                    else:
                                                        print("Lütfen doğru seçenek seçiniz!")
                                                else:
                                                    print("Bakiyeniz yetersiz!")
                                    else:
                                        print("Müşteri bulunamadı!")

                                elif secim2 == "4":
                                    miktar = int(input("Miktar : "))
                                    if miktar <= musteri.bakiye:
                                        musteri.bakiye -= miktar
                                        print("İşlem tamamlandı, paranızı alınız.")
                                    else:
                                        print("Bakiyeniz yetersiz!")

                                elif secim2 == "q" or "Q":
                                    break

                                else:
                                    print("Lütfen doğru seçeneği seçiniz!")
            else:
                print("Böyle bir ID bulunmamaktadır!")

        elif secim == "2":
            ID = input("Lütfen ID giriniz : ")
            ISIM = input("Lütfen isminizi giriniz : ")
            while True:
                PAROLA = input("Lütfen parolanızı giriniz : ")
                PAROLA_TEKRAR = input("Lütfen parolanızı tekrar giriniz : ")
                if PAROLA == PAROLA_TEKRAR:
                    print("Parola Eşleşiyor.")
                    break
                else:
                    print("Parolalar eşleşmiyor, Lütfen parolanızı tekrar giriniz!")

            banka.musteri_ol(ID,PAROLA, ISIM)


main()







