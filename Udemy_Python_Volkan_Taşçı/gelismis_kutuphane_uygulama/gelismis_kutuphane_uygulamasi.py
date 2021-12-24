import sqlite3

db = sqlite3.connect("kitaplar.sqlite")
imlec = db.cursor()

menu = """
    [1] Kitap Ara
    [2] Yazar Ara
"""

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

else:
    print("Lütfen doğru seçeneği seçiniz!")
    
db.close()
