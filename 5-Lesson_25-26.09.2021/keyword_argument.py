def hesapla(sayi1, sayi2, sayi3):
    print(sayi1 / sayi2 + (sayi3 * sayi1))

hesapla(sayi1=10,sayi2=11,sayi3=12) # keyword arguments

def vucut_kitle_endeksi(boy, kilo):
    print(kilo/(boy**2))

vucut_kitle_endeksi(1.76,78) # Bu şekilde yazarsan sıra önemli.
vucut_kitle_endeksi(boy=1.76, kilo=78) # Bu şekilde yazarsan sıra önemli değil
vucut_kitle_endeksi(kilo=78, boy=1.76) # Bu şekilde yazarsan sıra önemli değil

def vucut_kitle_endeksi(boy=1.80, kilo=80): # Default değeratadık
    print(kilo/(boy**2))

vucut_kitle_endeksi(boy=1.70) # Yukarıda default değer verdiğimiz için burada sadece bir değeri değiştirerek doğru değerleri alabiliriz.