#1. kulllanıcıadı ve şifrelerden oluşan bir listeniz (liste, dictionary, tuple) olacak
#2. kullanıcıadı ve şifre sorulacak, girilen kullanıcıadı ve şifreyi listede arayıp kontrol edilecek (tip : if)
#3. eğer kullanıcı 3 kez kulalnıcıadı ve şifresini hatalı girerse kullanıcı programdan atılacak 
#   ve daha sonra tekrar denemesi istenecek  (tip: while )


# personel_listesi = (("murat","12345"),("selim","12345"),("tugce","12345"))

#personel_listesi1 = {("murat","12345"),("selim","12345"),("tugce","12345")}

personel_listesi = ({"kullanici_adi":"murat", "sifre":"12345"},
                    {"kullanici_adi":"selim", "sifre":"12345"},
                    {"kullanici_adi":"tugce", "sifre":"12345"})

sayac = 1
programdan_ciksin_mi= False

while  sayac < 4 and programdan_ciksin_mi == False: #Sayaç neden 4'ten küçük?
   kullanici_adi = input("kullanıcı adınızı giriniz: ") #Kullanıcıdan kullanıcı adı istiyor.
   sifre = input("şifrenizi giriniz: ") #Kullanıcıdan şifre istiyor.
   indeks = 0 #İndex diye bir değer tanımlanıyor.
   personel_sayisi = len(personel_listesi) #personel listesinin uzunluğu (personel listesi uzunluğu = 3) personel sayısına atanıyor.

   while indeks < personel_sayisi : # Personel sayısı index ten büyük olduğu sürece dolanacak. Önce 0'dan dolanmaya başlar, 2'de bitirir.

      personel_list_kadi = personel_listesi[indeks]["kullanici_adi"] #personel listesi kullanıcı adı diye bir değere 
      personel_list_sifre = personel_listesi[indeks]["sifre"]

      if kullanici_adi == personel_list_kadi and sifre == personel_list_sifre:
         print("ola başarıyla giriş yaptınız") # Değerler birbirine eşit ise programa başarıylra giriş yaptığımızı yazdırıyor.
         programdan_ciksin_mi = True # programdan_ciksin_mi değerini True döndürüyor
         break #Bu if bloğundan çıkartıyor.

      if indeks == personel_sayisi - 1  :
         print("kullanıcı adınızı veya şifrenizi yanlış girdiniz")

      indeks = indeks + 1

   sayac = sayac + 1
   if sayac > 3 and programdan_ciksin_mi == False:
      print("kullanıcı ve adı ve şifresiniz 3 kez hatalı girdiniz.")