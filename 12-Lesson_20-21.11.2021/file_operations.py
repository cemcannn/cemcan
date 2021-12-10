# dosya = open(r"c:\dosya_yolu\dosya_adi.txt", "w") #bir dosyadaki path i yazma modunda açmak için bu kodu kullanıyoruz.

import os

dosya_yolu = os.path.expanduser()

print(dosya_yolu)

dosya=open(dosya_yolu, "w+")
dosya.write("")
print("------------------------------------ dosya üzerinde okuma")