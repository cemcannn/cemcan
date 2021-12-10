import os
from datetime import datetime
from typing import Callable
from Arac import *
from Insan import *
from Fatura import *

# Bazi dosyalari private yap.
# Insan class i icinde super kavrami olustur

class Ayar:
    def saat_ayari():
        print("Saat ve tarih ayarı yapıldı")

class Aciklama:
    def aciklama():
        print("""
        Araç satış sistemine hoşgeldiniz...
        
        Bu işlem araç satışı gerçekleştirmek için fatura kesmek üzere düzenlenmiştir.

        Fatura kesebilmek için öncelikle araç bilgileri, müşteri bilgilier ve personel bilgilerini girmeniz gerekmektedir.
        Araç bilgilerini girmek için ana menüden 1 numaralı araç yönetim menüsüne girmeniz gerekmektedir. Araç yönetim menüsünde 
        5 adet seçenek bulunmaktadır. 1. seçenekten araç ekleme, 2. seçenekten araç bulma, 3. seçenekten araç silme, 4. seçenekten 
        araç düzenleme yapabilir ve 5. seçenekten ana menüye dönebilirsiniz. Araç eklemek için araç kodu, araç markası, araç modeli, 
        araç yılı, araç kategorisi, araç fiyatı ve araç rengi bilgileri gerekmektedir. Bu bilgileri ekrana girdikten sonra aracınız 
        listeye eklenecektir. Araç  bulma ekranında ekrana gelen listeden araç kodunu girerek araç bilgilerine erişebilirsiniz. 
        Araç silme ekranında yine ekrana gelen listeden araç kodunu girerek ilgili aracı listeden silebilirsiniz fakat faturası 
        kesilmiş araç listeden silinmez. Araç düzenle ekranında yine listeden araç kodunu girerek ilgili aracın bilgilerini 
        düzenleyebilirsiniz.

        Müşteri bilgilerini girmek için ana menüden 2 numaralı müşteri yönetim menüsüne girmeniz gerekmektedir. Müşteri yönetim 
        menüsünde 5 adet seçenek bulunmaktadır. 1. seçenekten müşteri ekleme, 2. seçenekten müşteri bulma, 3. seçenekten müşteri silme, 
        4. seçenekten müşteri düzenleme yapabilir ve 5. seçenekten ana menüye dönebilirsiniz. Müşteri eklemek için müşteri TCKN, müşteri 
        adı, müşteri soyadı, müşteri adresi, müşteri ili, müşteri ilçesi ve müşteri telefon bilgileri gerekmektedir. Bu bilgileri ekrana 
        girdikten sonra müşteri listeye eklenecektir. Müşteri  bulma ekranında ekrana gelen listeden müşteri TCKN girerek müşteri 
        bilgilerine erişebilirsiniz. Müşteri silme ekranında yine ekrana gelen listeden müşteri TCKN girerek ilgili müşteriyi listeden 
        silebilirsiniz fakat faturası kesilmiş müşteri bilgileri listeden silinmez. Müşteri düzenle ekranında yine listeden müşteri TCKN 
        girerek ilgili aracın bilgilerini düzenleyebilirsiniz.        
        
        Personel bilgilerini girmek için ana menüden 3 numaralı personel yönetim menüsüne girmeniz gerekmektedir. Personel yönetim 
        menüsünde 5 adet seçenek bulunmaktadır. 1. seçenekten personel ekleme, 2. seçenekten personel bulma, 3. seçenekten personel silme, 
        4. seçenekten personel düzenleme yapabilir ve 5. seçenekten ana menüye dönebilirsiniz. Personel eklemek için müşteri TCKN, 
        personel adı, personel soyadı, personel adresi, personel ili, personel ilçesi, personel telefonu ve personel görev bilgileri 
        gerekmektedir. Bu bilgileri ekrana girdikten sonra personel listeye eklenecektir. Personel  bulma ekranında ekrana gelen listeden 
        personel TCKN girerek personel bilgilerine erişebilirsiniz. Personel silme ekranında yine ekrana gelen listeden personel TCKN 
        girerek ilgili personeli listeden silebilirsiniz fakat faturası kesilmiş personel bilgileri listeden silinmez. Personel düzenle 
        ekranında yine listeden personel TCKN girerek ilgili aracın bilgilerini düzenleyebilirsiniz.         
        
        Fatura bilgilerini girmek için ana menüden 4 numaralı fatura yönetim menüsüne girmeniz gerekmektedir. Fatura yönetim menüsünde 
        5 adet seçenek bulunmaktadır. 1. seçenekten fatura ekleme, 2. seçenekten fatura bulma, 3. seçenekten fatura silme, 4. seçenekten 
        fatura düzenleme yapabilir ve 5. seçenekten ana menüye dönebilirsiniz. Fatura eklemek için fatura numarası, fatura kesilecek 
        müşteri TCKN'si, fatura kesilecek araç kodu ve fatura kesecek personel bilgileri gerekmektedir. Bu bilgilerden fatura numarası 
        ekrana girildikten sırayla sistem müşteri listesini ekrana verecek, listeden fatura kesilecek müşterinin TCKN'sini girmenizi 
        isteyecek, sonrasında araç listesini ekrana verecek, listeden satılacak aracın araç kodunu girmenizi isteyecek, son olarak personel 
        listesini ekrana verecek, listeden fatura kesecek personel TCKN'sini ekrana girmenizi isteyecek ve fatura kesilerek sisteme kayıt 
        edilecektir. Fatura  bulma ekranında ekrana gelen listeden fatura numarası girerek fatura bilgilerine erişebilirsiniz. Fatura silme 
        ekranında yine ekrana gelen listeden fatura numarası girerek ilgili faturayı listeden silebilirsiniz. Fatura düzenle ekranında yine 
        listeden fatura numarsı girerek ilgili fatura bilgilerini düzenleyebilirsiniz.

        Ana menüden 6. seçeneği seçmeniz durumunda saat ve tarih ayarlarını yapabilirsiniz.

        Ana menüden 7. seçeneği seçmeniz durumunda ise sistemden çıkış yapabilirsiniz.      
        """)

class Menu_Yonetimi:
    def menu_yonetimi():
        input("Hoşgeldiniz. Devam etmek için bir tuşa basınız")
        while True:
            os.system("cls")
            print("""
            ===========================
            Ana Menü
            ===========================
            Lütfen bir seçenek seçiniz:
            (1) Araç yönetimi
            (2) Müşteri yönetimi
            (3) Personel yönetimi
            (4) Fatura yönetimi
            (5) Yardım
            (6) Saat/tarih ayarı
            (7) Çıkış
            ===========================
            """)
            secenek=input("Lütfen seçiminizi giriniz : ")   
            if secenek=="1":
                Arac_Yonetim_Sistemi.arac_yonetim_sistemi()
            elif secenek=="2":
                Musteri_Yonetim_Sistemi.musteri_yonetim_sistemi()
            elif secenek=="3":
                Personel_Yonetim_Sistemi.personel_yonetim_sistemi()
            elif secenek=="4":
                Fatura_Yonetim_Sistemi.fatura_yonetim_sistemi()
            elif secenek=="5":
                os.system("cls")
                Aciklama.aciklama()
                input("Devam etmek için enter tuşuna basınız.")            
            elif secenek=="6":
                os.system("cls")
                Ayar.saat_ayari()
                input("Devam etmek için enter tuşuna basınız.")             
            elif secenek=="7":
                os.system("cls")
                print("""
                ======================
                
                Güle güle...
                
                ======================
                """)
                input("")
                break

            else:
                print("""Lütfen doğru seçeneği seçiniz! ""","\a")
                input("Devam etmek için enter tuşuna basınız.")

if __name__ == "__main__":
    Menu_Yonetimi.menu_yonetimi()
else:
    print("Bu uygulama modül olarak çalışmaz.")
