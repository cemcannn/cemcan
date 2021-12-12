from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

driver_path = "/home/muratcabuk/chromedriver"

chrome_driver = webdriver.Chrome(executable_path=driver_path)


def test_merkez_bankasi_sube_sayisi():
    chrome_driver.get("https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Banka+Hakkinda/Iletisim/Subeler")
    sleep(5)
    print("Açılan sayfanın adı : " + chrome_driver.title)

    # kaynak koda bakılacak olursa elimizde sadece class var tabloyu yakalamk için  "MerkezBankasiTable table-striped table"
    tablo = chrome_driver.find_element(By.CSS_SELECTOR, "table[class='MerkezBankasiTable table-striped table']")

    t_rows = tablo.find_elements(By.TAG_NAME, "tr")

    for t_row in t_rows:
        col = t_row.find_elements(By.TAG_NAME, "td")[0]
        #sleep(1)
        print(col.text)

    chrome_driver.close()  # sadece üzerinde çalışılan tab veya pencereyi kapatır
    assert len(t_rows) == 21

#test_merkez_bankasi_sube_sayisi()