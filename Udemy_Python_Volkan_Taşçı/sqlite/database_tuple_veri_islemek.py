import sqlite3 # Önce sqlite uygulamasını import ediyoruz.
db = sqlite3.connect("kitaplar.sqlite") # kitaplar sqlite dosyasını oluşturuyoruz.

imlec = db.cursor() # database içinde imleç oluşturmak için.

veriler =[
        ("Ahmet Ümit","İstanbul Hatırası"),
        ("Yaşar Kemal","İnce Memed"),
        ("Paulo Coelho","Simyacı"),
        ("Paulo Coelho","Aldatmak")]

imlec.execute("CREATE TABLE IF NOT EXISTS kitaplik (yazar, kitap)") # imlecle bir komut oluşturmak için execute kullanıyoruz. Büyük küçük harf uyumu çok önemli değil. 1. Tablo oluştur, ikinci kısım tablo ismi(kitaplik), üçüncü kısım sütun başlıkları ve kaç sütun olduğunu belirtir(yazar,kitap).Eğer Koşullu tablo oluşturmak istersek: imlec.execute kısmına ("CREATE TABLE IF NOT EXISTS") olarak yazıyoruz bu da zaten oluşmuş bir tabloyu tekrar oluşturmaya çalıştığımızda hata mesajı almamızı engelliyor.

for i in veriler:
    imlec.execute("INSERT INTO 'kitaplik' VALUES (?,?)") # Tablo içine veri eklemek için insert into, hangi tabloya ekleneceği 'kitaplik' ve değerler values sonra parantez içine değerler giriliyor. Ayrıca yukarıdademet halinde verilen veriler de for i in şeklinde verilebilir.Ayrıca yukarıdademet halinde verilen veriler de for i in şeklinde verilebilir.

db.commit() # bu komuttan sonra yukarıdaki işlem işlenmiş oluyor.

#Tabloyu oluşturmak için uygulamayı çalıştırmak yeterli, sonrasında bunları görüntülemek için sqlite browser var, oradan yararlanabiliriz.

db.close()
