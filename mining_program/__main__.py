import os
from Firma import *
from Ruhsat import *
class Menu_Yonetimi:
    def menu_yonetimi():
        input("Hoşgeldiniz. Devam etmek için bir tuşa basınız")
        while True:
            os.system("cls")
            print("""
            ==========================================
            Ana Menü
            ==========================================
            (1) Firma Yönetim Menüsü                
            (2) Ruhsat Yönetim Menüsü                           
            (3) Çıkış            
            ==========================================
            """)
            secenek=input("Lütfen seçiminizi giriniz : ")   
            if secenek=="1":
                Firma_Yonetim_Sistemi.firma_yonetim_sistemi()
            elif secenek=="2":
                Ruhsat_Yonetim_Sistemi.ruhsat_yonetim_sistemi()
            elif secenek=="3":
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



