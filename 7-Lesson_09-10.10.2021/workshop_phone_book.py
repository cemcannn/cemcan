
class Kisi:
    def  __init__(self, adi, soyadi):
        self.adi            = adi
        self.soyadi         = soyadi

class Telefon:
    def  __init__(self, telefon_cinsi,telefon):
        self.telefon_cinsi  = telefon_cinsi
        self.telefon        = telefon

class Telefon_rehberi:
    kisiler = []
    def  __init__(self, kisi, telefon):
        self.kisi = kisi
        self.telefon = telefon
        self.kisiler.append(self)

    @classmethod
    def telefon_rehberini_getir(cls):
        return cls.kisiler

    @classmethod
    def kisi_sil(cls, kisi_indeks_no) -> bool :
        cls.kisiler.pop(kisi_indeks_no)
        return True

while 1==1:
    secenek = input(
    """
    -------------------------------------------------
    || 1. Telefon rehberi                          ||
    || 2. Rehberde Kişi ara                        ||
    || 3. Kişi ekle                                ||
    || 4. Kişi sil                                 ||
    || 5. Kişi numara güncelleme                   ||
    || 6. Mesaj at                                 ||
    || 7. Arama yap                                ||
    || 8. Hesap makinesi (Basit)                   ||                                         
    || Q. Çıkış yap                                ||
    -------------------------------------------------
    Lütfen yapmak istediğiniz işlemi seçiniz : 
    """)

    if secenek == "1":
        template = "Kişi Adı : {},Kişi Soyadı : {}, Telefon Cinsi : {}, Telefon Numarası : {}"
        telefon_rehberi=Telefon_rehberi.telefon_rehberini_getir()
        for kisiler in telefon_rehberi:
            print(kisiler.kisi.adi,kisiler.kisi.soyadi, kisiler.telefon.telefon_cinsi,kisiler.telefon.telefon)

    elif secenek == "2":
        pass

    elif secenek == "3":
        kisi = Kisi(input("Kişi adını giriniz : "),input("Kişi soyadı giriniz : "))
        telefon = Telefon(input("Telefon cinsini giriniz : "),input("Kişi telefon numarası giriniz : "))

        telefon_kaydi = Telefon_rehberi(kisi,telefon)
        print("Kayıt yapıldı.")

    elif secenek == "4":
        pass

    elif secenek == "5":
        pass

    elif secenek == "6":
        break
  
    elif secenek == "7":
        pass

    elif secenek == "8":
        pass

    elif secenek == "q" or secenek == "Q":
        break  

    else:
        print("lütfen doğru seçeneği giriniz")