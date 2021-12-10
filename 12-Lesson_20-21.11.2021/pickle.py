import pickle
import os

# linux ve mac için home klasörü
print(os.path.expanduser('~'))

# windows versiyonu
#exp_var1 = os.path.expandvars("C:\Users\$USERNAME")


dosya_yolu = os.path.expanduser('~') + "/dosyalar/veriler.data"

liste= [[1,2,3,4],"a","b","c",["ahmet","mehmet"],1,2,3]
# dump_liste = "1010110000100010010101010101010101010110101010"

# wb nedemek bakabilirsiniz : https://python-istihza.yazbel.com/temel_dosya_islemleri.html
with open(dosya_yolu ,"wb") as f:
    # dump_liste = "1010110000100010010101010101010101010110101010"
    pickle.dump(liste,f)

diskten_okunan_liste=[]

with open(dosya_yolu,"rb") as f:
    diskten_okunan_liste = pickle.load(f)

print(diskten_okunan_liste)

print(type(diskten_okunan_liste))

diskten_okunan_liste.append("yeni obje")

print(diskten_okunan_liste)

diskten_okunan_liste.pop(2)

print(diskten_okunan_liste) # b harfi silindi


with open(dosya_yolu ,"wb") as f:
    # dump_liste = "1010110000100010010101010101010101010110101010"
    pickle.dump(diskten_okunan_liste,f)


with open(dosya_yolu,"rb") as f:
    diskten_okunan_liste = pickle.load(f)

print(diskten_okunan_liste)


