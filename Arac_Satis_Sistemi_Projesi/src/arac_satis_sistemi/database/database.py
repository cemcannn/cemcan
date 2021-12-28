import sqlite3
import os

current_directory =  os.getcwd()
veritabanim = sqlite3.connect('{}\\My_Projects\\arac_satis_sistemi_projesi\\src\\arac_satis_sistemi\\database\\veritabanim.sqlite'.format(current_directory))

imlec = veritabanim.cursor()

imlec.execute("""CREATE TABLE IF NOT EXISTS araclar
                (Benzersiz_kod INTEGER NOT NULL, 
                Seri_no STRING NOT NULL, 
                Marka STRING NOT NULL, 
                Model STRING NOT NULL, 
                Fiyat INTEGER NOT NULL, 
                Renk STRING NOT NULL, 
                Silindir INTEGER NOT NULL,
                PRIMARY KEY("Benzersiz_kod" AUTOINCREMENT)
                )""")

imlec.execute("""CREATE TABLE IF NOT EXISTS personeller
                (Benzersiz_kod INTEGER NOT NULL, 
                Personel_TCKN INTEGER NOT NULL, 
                Adi STRING NOT NULL, 
                Soyadi STRING NOT NULL, 
                Adres STRING NOT NULL, 
                Telefon INTEGER NOT NULL, 
                Gorev STRING NOT NULL,                
                PRIMARY KEY("Benzersiz_kod" AUTOINCREMENT)
                )""")

imlec.execute("""CREATE TABLE IF NOT EXISTS musteriler
                (Benzersiz_kod INTEGER NOT NULL, 
                Musteri_TCKN INTEGER NOT NULL, 
                Adi STRING NOT NULL, 
                Soyadi STRING NOT NULL, 
                Adres STRING NOT NULL, 
                Telefon INTEGER NOT NULL,
                PRIMARY KEY("Benzersiz_kod" AUTOINCREMENT)
                )""")

imlec.execute("""CREATE TABLE IF NOT EXISTS faturalar
                (Benzersiz_kod INTEGER NOT NULL, 
                Fatura_no INTEGER NOT NULL, 
                Arac STRING NOT NULL, 
                Musteri STRING NOT NULL, 
                Personel STRING NOT NULL, 
                Tutar INTEGER NOT NULL, 
                Tarih STRING NOT NULL,                
                PRIMARY KEY("Benzersiz_kod" AUTOINCREMENT)
                )""")

veritabanim.commit()
veritabanim.close()
