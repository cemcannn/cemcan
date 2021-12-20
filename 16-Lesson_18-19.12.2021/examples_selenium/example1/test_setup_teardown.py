from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

driver_path = "/home/muratcabuk/chromedriver"


@pytest.fixture
def chrome_driver():
    chrome_driver = webdriver.Chrome(executable_path=driver_path)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()



def test_merkez_bankasi_sube_sayisi(chrome_driver):

    chrome_driver.get("https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Banka+Hakkinda/Iletisim/Subeler")
    
    print("Açılan sayfanın adı : " + chrome_driver.title)
    
    #kaynak koda bakılacak olursa elimizde sadece class var tabloyu yakalamk için  "MerkezBankasiTable table-striped table"
    tablo= chrome_driver.find_element(By.CSS_SELECTOR,"table[class='MerkezBankasiTable table-striped table']")
    
    t_rows = tablo.find_elements(By.TAG_NAME,"tr")
    time.sleep(3)
    for t_row in t_rows:
        col = t_row.find_elements(By.TAG_NAME, "td")[0]
        print(col.text)

    assert len(t_rows) == 21
    



def test_merkez_bankasi_sube_sayisi_hata(chrome_driver):


    chrome_driver.get("https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Banka+Hakkinda/Iletisim/Subeler")
    
    print("Açılan sayfanın adı : " + chrome_driver.title)
    
    #kaynak koda bakılacak olursa elimizde sadece class var tabloyu yakalamk için  "MerkezBankasiTable table-striped table"
    tablo= chrome_driver.find_element(By.CSS_SELECTOR,"table[class='MerkezBankasiTable table-striped table']")
    
    t_rows = tablo.find_elements(By.TAG_NAME,"tr")
    time.sleep(3)
    for t_row in t_rows:
        col = t_row.find_elements(By.TAG_NAME, "td")[0]
        print(col.text)
    

    assert len(t_rows) == 20

    





def test_merkez_bankasi_sube_sayisi_hata2(chrome_driver):


    chrome_driver.get("https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Banka+Hakkinda/Iletisim/Subeler")
    
    print("Açılan sayfanın adı : " + chrome_driver.title)
    
    #kaynak koda bakılacak olursa elimizde sadece class var tabloyu yakalamk için  "MerkezBankasiTable table-striped table"
    tablo= chrome_driver.find_element(By.CSS_SELECTOR,"table[class='MerkezBankasiTable table-striped table']")
    
    t_rows = tablo.find_elements(By.TAG_NAME,"tr")
    time.sleep(3)
    for t_row in t_rows:
        col = t_row.find_elements(By.TAG_NAME, "td")[0]
        print(col.text)
    

    assert len(t_rows) == 19



