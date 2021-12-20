
sqlite cli içindeyken

```sqlite

.help
# komutların listesi gelir

.open "/home/muratcabuk/veritabani.db"

.databases
#main: /home/muratcabuk/veritabani.db r/w

.dbinfo
# database hakkında tüm detayları doker

.tables
# bütün tabloları doker

.show
# aktif bağlantıda kullanılan ayarların lsiteini doker. orneğin üzerinde çalışılan db nin path i

.mode table
# output değiştirir. üstteki komut table a çeviriyor.

.schema
# tabloların oluşturlma scriplerini ekrana getirir. table ismi kullanılırsa o tabloyununkini getirir.

.read myscript.sql
# script dosyasını okur

.indexes
# bütün indexleri listeler. eğer tablo ismi kullanılırsa o tablonunkileri getirir


.quit 
# çıkış yapar

```
birden fazla db ile çalışmakda mümkün 

```
ATTACH DATABASE 'testDB.db' as 'TEST';
```

# Primary key ve Foreign key
- One-To-Many, Many-To-Many Relation
- Unique Identifier


#### DML, DDL, DCL, TCL

- **DDL (Data Definition Language):** Veri Tanımlama Dili (DDL) deyimleri tabloları, veritabanı yapısı veya şema tanımlamak için kullanılır.
Bunlardan bazıları;

    - CREATE: Veritabanındaki nesneleri oluşturmak için kullanılır.
    - ALTER: Veritabanı nesnelerinin yapısını değiştirmek için kullanılır.
    - DROP: Veritabanındaki nesneleri silmek ya da başka bir ifadeyle ilgili nesneleri bütünüyle kaldırmak için kullanılır.
    - TRUNCATE: Kayıtlar için ayrılan tüm boşluklar dahil, bir tablodaki tüm kayıtları kaldırılır
    - COMMENT: Veri sözlüğüne yorum eklemek için kullanılır.
    - RENAME: Bir nesneyi yeniden adlandırmak için kullanılır.

- **DML (Data Manipulation Language):** Veri İşleme Dili (DML) deyimleri tablo ya da şema nesneleri içindeki verileri yönetmek için kullanılır.
Bunlardan bazıları;

    - SELECT: Veritabanından kayıt çekmek için kullanılır.
    - INSERT: Tabloya kayıt ya da kayıtları eklemek için kullanılır.
    - UPDATE: Tablodaki kayıt ya da kayıtları güncellemek için kullanılır.
    - DELETE: Tablodan kayıt ya da kayıtları silmek için kullanılır (Veriler silinse de ancak kapladığı alan kalır)
    - MERGE: UPSERT işlemi (ekleme veya güncelleme), başka bir ifadeyle birleştirme yapar.
    - CALL: PL/SQL veya Java alt programını çalıştırır.
    - EXPLAIN PLAN: Verilere erişim yolunun detaylarını açıklamak için kullanılır.
    - LOCK TABLE: Kontrolü eş zamanlılığı sağlamak için kullanılır.

- **DCL (Data Control Language):** Veri Kontrol Dili (DCL) deyimleri yetkilendirme ya da ayrıcalıkları belirlemek için kullanılır.
Bunlardan bazıları;
    - GRANT: Belirli bir kullanıcı ya da gruba veritabanının belirtilen nesnelerine erişim ayrıcalıklarını verir.
    - REVOKE - GRANT: komutu ile verilen ayrıcalıkların bir kısmını ya da tümünü geri almak için kullanılır.

- **TCL (Transaction Control):** İşlem Kontrol (TCL) deyimleri DML ifadeleri tarafından yapılan değişiklikleri yönetmek için kullanılır.
Bunlardan bazıları;
    - COMMIT: Yapılanları kalıcı hale getirir. İşin tamamlanmasını sağlar.
    - SAVEPOINT: Daha sonra geri dönülecek bir dönüş noktası belirler.
    - ROLLBACK: Son COMMIT'e kadar olan yeri geri alır.


### CREATE TABLE


one to many 


```sql

-- CREATE TABLE yazar (

--     yazar_id INTEGER NOT NULL UNIQUE, PRIMARY KEY("pk_yazar_id" AUTOINCREMENT),
--     ad VARCHAR NOT NULL,
--     soyad VARCHAR NOT NULL
-- );


-- CREATE TABLE kitap (
--     kitap_id INTEGER NOT NULL UNIQUE, PRIMARY KEY("kitap_id" AUTOINCREMENT),
--     /*yazar_id INTEGER REFERENCES yazar,*/ /* foreign key */
--     yazar_id INTEGER NOT NULL, FOREIGN KEY("yazar_id") REFERENCES yazar(yazar_id)
--     kitap_adi VARCHAR
-- );

-- diğer version



CREATE TABLE yazar (

    yazar_id INTEGER NOT NULL UNIQUE, 
    ad VARCHAR NOT NULL,
    soyad VARCHAR NOT NULL,
    CONSTRAINT "pk_yazar_id" PRIMARY KEY("yazar_id" AUTOINCREMENT)
);

CREATE TABLE kitap (
    kitap_id INTEGER NOT NULL UNIQUE,
    yazar_id INTEGER NOT NULL,
    kitap_adi TEXT NOT NULL,
    CONSTRAINT "fk_yazar_id" FOREIGN KEY("yazar_id") REFERENCES yazar(yazar_id),
    CONSTRAINT "pk_kitap_id" PRIMARY KEY("kitap_id" AUTOINCREMENT)
);


```

Many To Many


```sql
CREATE TABLE yazar (
    yazar_id INTEGER NOT NULL UNIQUE, 
    ad VARCHAR NOT NULL,
    soyad TEXT NOT NULL,
    CONSTRAINT "pk_yazar_id_id" PRIMARY KEY("yazar_id" AUTOINCREMENT)
);


CREATE TABLE yayinevi (
    yayinevi_id INTEGER NOT NULL UNIQUE,
    yayinevi_adi VARCHAR NOT NULL,
    CONSTRAINT "pk_yayinevi_id" PRIMARY KEY("yayinevi_id" AUTOINCREMENT)

);


CREATE TABLE "yazar_yayinevi_line" (
    yazar_id INTEGER NOT NULL,
    yayinevi_id	INTEGER NOT NULL,
    FOREIGN KEY("yayinevi_id") REFERENCES "yayinevi"("yayinevi_id"),
    FOREIGN KEY("yazar_id") REFERENCES "yazar"("id"),
    CONSTRAINT "pk_id" PRIMARY KEY("yazar_id","yayinevi_id")
);

```

### ALTER TABLE

tabloyu değiştirmek için kullanılır

```sql

ALTER TABLE araclar RENAME TO arabalar;

ALTER TABLE araclar ADD COLUMN fiyat REAL;

```

### DROP TABLE

tablo silmek için

```sql
DROP TABLE araclar;


```

### CREATE INDEX

```sql
-- araçlar tablosu üzerinde marka sütunu içi imndex oluşturdduk
CREATE INDEX "ix_marka" ON "araclar" (
	"marka"	ASC
);

DROP INDEX  ix_marka;

```



## Kaynaklar
- https://sqlite.org/cli.html