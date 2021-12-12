from selenium import webdriver
#from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "/home/muratcabuk/chromedriver"

chrome_driver = webdriver.Chrome(executable_path=driver_path)

chrome_driver.get("https://www.google.com")

print("Açılan sayfanın adı : " + chrome_driver.title)

#arama_kutusu = chrome_driver.find_element_by_name("q")
arama_kutusu= chrome_driver.find_element(By.NAME,"q")
sleep(5)
arama_kutusu.send_keys("python")

arama_kutusu.send_keys(Keys.RETURN)

sleep(5)

#page_2 = chrome_driver.find_element_by_link_text("2")
page_2= chrome_driver.find_element(By.LINK_TEXT,"2")

page_2.click()

print("sayfa 2 y gidildi")

sleep(1)
chrome_driver.back()

print("anasayfaya geri dönüldü")

try:
        # selenium ile bekleme yapmak daha mantıklı
    element = WebDriverWait(chrome_driver, 2).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    print("myDynamicElement elementi bulunamadı")
    #chrome_driver.quit() # bütün pencere ve tabları kapatır

sleep(5)

chrome_driver.close() # sadece üzerinde çalışılan tab veya pencereyi kapatır