import fonksiyonlar

def test_mesaj_dondur():
   mesaj = fonksiyonlar.mesaj_dondur()
   assert mesaj == "merhaba"

def test_toplama():
   num = fonksiyonlar.toplama()
   assert num == 5

def test_toplama2():
   num = fonksiyonlar.toplama2()
   assert num == 6