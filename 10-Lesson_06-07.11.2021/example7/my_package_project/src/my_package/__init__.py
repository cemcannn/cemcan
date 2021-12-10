from .sub_pkg1 import *
from .sub_pkg2 import *
from .main_pkg import *


__all__ = ["module1","module2"] # ancak sub_pk2 de module1 yüklenmediği için burada sadecce sub_pkg1 deki module1 ler yüklenecek

print(__name__ + " yüklendi")


module1.fonksiyon()