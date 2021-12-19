import sqlite3

#linux ve mac
# veritabanim = sqlite3.connect('/home/muratcabuk/projects/data/veritabani_test.sqlite')

# #windows
veritabanim = sqlite3.connect('c:\\veritabani\\veritabani_test.sqlite')


imlecim = veritabanim.cursor()


sql="""CREATE TABLE IF NOT EXISTS 'araclar'
                    ('arac_id INTEGER NOT NULL PRIMARY KEY', 
                        'arac_marka VARCHAR', 
                        'arac_model VARCHAR')"""


# # arac_id | arac_marka | arac_model # oluşacak tablo

imlecim.execute(sql)
veritabanim.commit()
veritabanim.close()

############################################## veri kaydetmek

veritabanim = sqlite3.connect('/home/muratcabuk/projects/data/veritabani_test.sqlite')
imlecim = veritabanim.cursor()

insert_sql= """INSERT INTO araclar VALUES (11, 'Ford', 'Focus')"""

imlecim.execute(insert_sql)


veritabanim.commit()
veritabanim.close()

##########################################33  veri okumak


veritabanim = sqlite3.connect('/home/muratcabuk/projects/data/veritabani_test.sqlite')
imlecim = veritabanim.cursor()

select_sql= """SELECT * FROM araclar"""

imlecim.execute(select_sql)

veriler = imlecim.fetchall()

print("------------------------- veri tipi:" + str(type(veriler)))

print(veriler)


veritabanim.commit()
veritabanim.close()
