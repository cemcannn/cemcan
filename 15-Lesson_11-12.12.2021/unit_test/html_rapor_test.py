# html rapor almak için kullanılan module
# https://pytest-html.readthedocs.io/en/latest/user_guide.html
# windows : pip install pytest-html
# mac ve linux : pip3 install pytest-html

# çalıştırmak için
#  pytest html_rapor_test.py  --html=report.html --self-contained-html --maxfail=10

import html_rapor
import pytest

@pytest.mark.parametrize("beklenen_toplama_sonucu,toplanacak_sayilar",[(3,(1,2)),(4,(3,2)),(-3,(-1,-2)),(0,(1,-1))])
def test_toplama(beklenen_toplama_sonucu:int, toplanacak_sayilar:list):
    gercek_toplama_sonucu = html_rapor.toplama(toplanacak_sayilar[0],toplanacak_sayilar[1])
    assert gercek_toplama_sonucu == beklenen_toplama_sonucu



@pytest.mark.parametrize("sayi,beklenen_carpma_sonucu",[(3,7),(5,10),(-3,-6),(0,0)])
def test_carpma(beklenen_carpma_sonucu:int, sayi:int):
    gercek_carpma_sonucu = html_rapor.carpma(sayi)
    assert gercek_carpma_sonucu == beklenen_carpma_sonucu
