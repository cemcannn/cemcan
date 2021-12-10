import sqlite3 # Önce sqlite uygulamasını import ediyoruz.
db = sqlite3.connect("kitaplar.sqlite") # kitaplar sqlite dosyasını oluşturuyoruz.

imlec = db.cursor() # database içinde imleç oluşturmak için.

imlec.execute("SELECT * FROM 'kitaplik'") # kitaplik dosyasından her şeyi çekiyor  fakat nereye çekeceğimiz henüz belli değil.

veriler =imlec.fetchall() # fetchall  imleç metodu, eğer tek tek çağırmak istersek fetchone fonksiyonunu giriyoruz. Ya da kaç tane çağırmak istersen fetchmany(5) mesela 5 tane çağırmak için parantez içine 5 giriyoruz.

for veri in veriler:
    print(veri)

db.close()



