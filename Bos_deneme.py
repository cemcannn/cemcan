import sqlite3

# al = sqlite3.connect("araclar.sqlite")
# imlec = al.cursor()
# imlec.execute("CREATE TABLE IF NOT EXISTS araclar (id, Seri_no, Marka, Model, Fiyat, Renk, Silindir)")
# imlec.execute("INSERT INTO araclar VALUES (?,?,?,?,?,?,?)",("392524","A123-4567","fds","sada",4164,"sfds",654))
# al.commit()
# al.close()

# benzersiz_kod = input("sdsd")
# al = sqlite3.connect("araclar.sqlite")
# imlec = al.cursor()
# imlec.execute("DELETE FROM 'araclar' WHERE id = '{}'".format(benzersiz_kod))
# al.commit()
# al.close()

serino = int(input("sdfdsf"))
al = sqlite3.connect("araclar.sqlite")
imlec = al.cursor()
imlec.execute("SELECT * FROM 'araclar' WHERE 'Seri_no' = '{}'".format(serino))
arac = imlec.fetchall()
al.close()        
if serino != None:
    print("dfdf")