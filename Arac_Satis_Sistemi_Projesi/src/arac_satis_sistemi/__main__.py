import menu_yonetimi # Ana dosya menu yönetimi dosyasını çekiyor

if __name__ == "__main__": # Eğer ana dosya ise çalışıyor, modül ise çalışmıyor.
    menu_yonetimi.ana_menu_getir()
else:
    print("Bu Uygulama Module Olarak Kullanılamaz.")