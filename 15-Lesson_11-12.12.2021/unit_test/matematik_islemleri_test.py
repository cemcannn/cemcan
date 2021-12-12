import matematik_islemleri
import pytest

@pytest.mark.parametrize("beklenen_toplama_sonucu,toplanacak_sayilar",[(3,(1,2)),(5,(3,2)),(-3,(-1,-2)),(0,(1,-1))])
def test_toplama(beklenen_toplama_sonucu:int, toplanacak_sayilar:list):
    gercek_toplama_sonucu = matematik_islemleri.toplama(toplanacak_sayilar[0],toplanacak_sayilar[1])
    assert gercek_toplama_sonucu == beklenen_toplama_sonucu
