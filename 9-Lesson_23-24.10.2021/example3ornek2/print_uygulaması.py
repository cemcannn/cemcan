class PrintApp():
    def programi_calistir():
        while True:
            metin = input("metin giriniz : ")
            print(metin)
            secenek = input("çıkmak için h, devam etmek için e ye basınız.")
            if secenek == "h":
                break



if __name__ == "__main__":
    PrintApp.programi_calistir()
else:
    print("Bu uygulama modül olarak kullanılamaz. Doğrudan çalışır.")