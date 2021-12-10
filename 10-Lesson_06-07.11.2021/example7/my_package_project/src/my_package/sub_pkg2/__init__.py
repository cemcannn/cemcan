# bu dosya konulmasa da olur çünki burada namespace package sistemini uyguluyoruz. 
# ancak python 3.2 ve üstü için lazım
# https://www.python.org/dev/peps/pep-0420/
# https://docs.python.org/3/reference/import.html#regular-packages


from .sub_pkg2_pkg1 import *
from .sub_pkg2_pkg2 import *

# __all__= ["module1","module2"]

__all__= ["module2"] # module1 in üst paketler tarafından kullanılmasını sub_pkg2_pkg1 ve sub_pkg2_pkg2 için de engelledik
                     # eğer sadece sub_pkg2_pkg1 için engellmek isteseydik burada module1 e izin verip sub_pkg2_pkg1 içindeki __init__.py dosyaında module1 i yazmamalıydık
print(__name__ + " yüklendi")

