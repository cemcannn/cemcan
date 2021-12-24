import sqlite3

while True:
    print("""
            1 araç ekle
            2 araç sil
            3 araç benzersiz
            4 araç seri no
            5 araç listesi
            6 araç düzenle
""")
    sayi = input("sds")
    if sayi == "1": # Arac ekle fonksiyonu keyword arguments olarak arac parametresi Araç classı olarak tanımlanıyor.
        al = sqlite3.connect("araclar.sqlite")
        imlec = al.cursor()
        imlec.execute("""CREATE TABLE IF NOT EXISTS 'araclar' 
                    (Benzersiz_kod INTEGER NOT NULL, 
                    Seri_no NOT NULL, 
                    Marka STRING NOT NULL, 
                    Model STRING NOT NULL, 
                    Fiyat INTEGER NOT NULL, 
                    Renk STRING NOT NULL, 
                    Silindir INTEGER NOT NULL)""")

        imlec.execute("INSERT INTO 'araclar' VALUES (?,?,?,?,?,?,?)",("56936","A123-2478","TOYOTA","COROLLA",120000,"KIRMIZI",1600))
        al.commit()
        al.close()

    if sayi == "2":
        benzersiz_kod = input("dsdsd:")
        al = sqlite3.connect("araclar.sqlite")
        imlec = al.cursor()
        imlec.execute("DELETE FROM 'araclar' WHERE 'Benzersiz_kod' = '56936'")
        al.commit()
        al.close()

    if sayi == "3": # Araç getir fonksiyonunu benzersiz koddan çağırıyor.
        benzersiz_kod = input("dsdsd:")
        al = sqlite3.connect("araclar.sqlite")
        imlec = al.cursor()
        imlec.execute("SELECT * FROM 'araclar' WHERE 'Benzersiz_kod' = '{}'".format(benzersiz_kod))
        arac = imlec.fetchone()
        al.close()                             
        print(arac)

    if sayi == "4": # Araç getir fonksiyonunu seri numaradan getiriyor.
        serino = input("dsdsd:")
        al = sqlite3.connect("araclar.sqlite")
        imlec = al.cursor()
        imlec.execute("SELECT * FROM 'araclar' WHERE 'Seri_no' = '{}'".format(serino))
        arac = imlec.fetchone()
        al.close()        
        print(arac)

                        
    if sayi == "5":
        al = sqlite3.connect("araclar.sqlite")
        imlec = al.cursor()
        sorgu = "SELECT * FROM araclar"
        imlec.execute(sorgu)
        arac_listesi = imlec.fetchall()
        print(arac_listesi)

    if sayi == "6":
        al = sqlite3.connect("araclar.sqlite")
        imlec = al.cursor()
        imlec.execute("UPDATE 'araclar' set ({},{},{},{},{},{},{}) WHERE Seri_no = '{}'".format(arac.benzersiz_kod,arac.serino,arac.marka,arac.model,arac.fiyat,arac.renk,arac.silindir,arac.benzersiz_kod))
        al.commit()
        al.close()

