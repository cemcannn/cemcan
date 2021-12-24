import sqlite3

db = sqlite3.connect("kitaplar.sqlite")
imlec = db.cursor()

menu = """
    [1] Kitap Ara
    [2] Yazar Ara
    [3] Sil
    [4] Ekle
    [5] kitaplar
"""
while True:
        print(menu)

        islem = input("İşleminiz : ")

        if islem == "1":
            isim = input("Kitap adını giriniz : ")
            sorgu = "SELECT * FROM 'kitaplar' WHERE kitap = '{}'".format(isim)
            imlec.execute(sorgu)
            veriler = imlec.fetchall()
            for i in veriler:
                print(i)
            
        elif islem == "2":
            isim = input("Yazar ismi giriniz  : ")
            sorgu = "SELECT * FROM 'kitaplar' WHERE yazar = '{}'".format(isim)
            imlec.execute(sorgu)
            veriler = imlec.fetchall()
            for i in veriler:
                print(i)
            

        elif islem == "3":
            isim = input("Yazar ismi giriniz  : ")
            sorgu = "DELETE FROM 'kitaplar' WHERE yazar = {}".format(isim)
            imlec.execute(sorgu)
            veriler = imlec.fetchone()
            db.commit()

        elif islem == "4":
            yazar = input("yazar girin")
            kitap = input("kitap girin")
            imlec.execute("CREATE TABLE IF NOT EXISTS kitaplik (yazar, kitap)")
            imlec.execute(f'INSERT INTO kitaplar VALUES ("{yazar}","{kitap}")')
            db.commit() 

        elif islem == "5":
            sorgu = "SELECT * FROM 'kitaplar'" 
            imlec.execute(sorgu)
            veriler = imlec.fetchall()
            for i in veriler:
                print(i)
            
        else:
            print("Lütfen doğru seçeneği seçiniz!")
            

