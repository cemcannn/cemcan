from .arac import Arac # arac modülünden Arac class ını import ediyoruz.
import sqlite3

def arac_ekle(arac:Arac): # Arac ekle fonksiyonu keyword arguments olarak arac parametresi Araç classı olarak tanımlanıyor.
    al = sqlite3.connect("araclar.sqlite")
    imlec = al.cursor()
    imlec.execute("""CREATE TABLE IF NOT EXISTS 'araclar' 
                (Benzersiz_kod INTEGER NOT NULL PRIMARY KEY, 
                Seri_no INTEGER NOT NULL, 
                Marka STRING NOT NULL, 
                Model STRING NOT NULL, 
                Fiyat INTEGER NOT NULL, 
                Renk STRING NOT NULL, 
                Silindir INTEGER NOT NULL)""")

    imlec.execute("INSERT INTO 'araclar' VALUES (?,?,?,?,?,?,?)",(arac.benzersiz_kod,arac.serino,arac.marka,arac.model,arac.fiyat,arac.renk,arac.silindir))
    al.commit()
    al.close()

def arac_sil(benzersiz_kod:int):
    al = sqlite3.connect("araclar.sqlite")
    imlec = al.cursor()
    imlec.execute("DELETE FROM 'araclar' WHERE 'Benzersiz_kod' = '{}'".format(benzersiz_kod))
    al.commit()
    al.close()

def arac_getir_benzersizkod(benzersiz_kod:int) -> Arac: # Araç getir fonksiyonunu benzersiz koddan çağırıyor.
    al = sqlite3.connect("araclar.sqlite")
    imlec = al.cursor()
    imlec.execute("SELECT * FROM 'araclar' WHERE 'Benzersiz_kod' = '{}'".format(benzersiz_kod))
    arac = imlec.fetchone()
    al.close()                             
    print(arac)

def arac_getir_serino(serino:str) -> Arac: # Araç getir fonksiyonunu seri numaradan getiriyor.
    if :
        al = sqlite3.connect("araclar.sqlite")
        imlec = al.cursor()
        imlec.execute("SELECT * FROM 'araclar' WHERE 'Seri_no' = '{}'".format(serino))
        arac = imlec.fetchall()
        al.close()        
        if serino != None:
            return arac
        return None
    except:
        return None
                    
def arac_listele() -> list():
    al = sqlite3.connect("araclar.sqlite")
    imlec = al.cursor()
    sorgu = "SELECT * FROM araclar"
    imlec.execute(sorgu)
    arac_listesi = imlec.fetchall()
    return arac_listesi

def arac_duzenle(arac:Arac):
    al = sqlite3.connect("araclar.sqlite")
    imlec = al.cursor()
    imlec.execute("UPDATE 'araclar' set ({},{},{},{},{},{},{}) WHERE Seri_no = '{}'".format(arac.benzersiz_kod,arac.serino,arac.marka,arac.model,arac.fiyat,arac.renk,arac.silindir,arac.benzersiz_kod))
    al.commit()
    al.close()