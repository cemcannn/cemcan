from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
from time import sleep

driver_path = "/home/muratcabuk/chromedriver"

def haberlercom_dan_haber_topla():

    chrome_driver = webdriver.Chrome(executable_path=driver_path)
    chrome_driver.maximize_window()

    

    sayfa_sayisi = 3
    haber_detay_listesi=[]

    for i in range(1,sayfa_sayisi+1):
        if i == 1:
            chrome_driver.get("https://www.haberler.com/turkiye/")
        else:
            chrome_driver.get("https://www.haberler.com/turkiye/s" + str(i))

        print("Açılan sayfanın adı : " + chrome_driver.title)

        haber_listesi = chrome_driver.find_elements(By.CLASS_NAME, "color-general")

        for i in haber_listesi:
            haber_baslik=i.text

            #haber_detay= i.find_element(By.CLASS_NAME,"hbBoxMainText").text
            haber_detay = i.text
            haber_detay_listesi.append([haber_baslik,haber_detay])

    sleep(5)


haberlercom_dan_haber_topla()