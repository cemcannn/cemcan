from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
from time import sleep

driver_path = "/home/muratcabuk/chromedriver"

def kitap_bilgilerini_topla():

    chrome_driver = webdriver.Chrome(executable_path=driver_path)
    chrome_driver.maximize_window()

    chrome_driver.get("https://demoqa.com/books")
    print("Açılan sayfanın adı : " + chrome_driver.title)

    kitap_listesi_element = chrome_driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    kitap_link_listesi=[]
    kitap_detay_listesi = []




    for i in kitap_listesi_element:
        satir_hucre_listesi = i.find_elements(By.CLASS_NAME, "rt-td")
        if satir_hucre_listesi[1].text != " ":
            kitap_link = satir_hucre_listesi[1].find_element(By.TAG_NAME,"a").get_attribute('href')
            kitap_link_listesi.append(kitap_link)

    for i in kitap_link_listesi:
        chrome_driver.get(i)

        elements = chrome_driver.find_elements(By.ID,"userName-value")

        isbn = elements[0].text
        title = elements[1].text
        author = elements[3].text
        pages= elements[5].text
        website = elements[7].text

        kitap_detay_listesi.append([isbn,title,author,pages,website])


    import os
    dosya_adi = os.getcwd() + "/kitaplar.txt"
    if(os.path.exists(dosya_adi)):
        dosya = open(dosya_adi, "a")    
    else:
        dosya = open(dosya_adi, "w")

    for i in kitap_detay_listesi:
        dosya_read_mode = open(dosya_adi, "r")

        dosya_read_mode.seek(0)
        for t in dosya_read_mode.readlines():
            if t.find(i[0]):
                print("dosyada var", i[0])
            else:
                dosya.seek(len(dosya))
                dosya.write(f"isbn={i[0]},title={i[1]},author={i[2]}, pages={i[3]}, website={i[4]}\n")
        dosya_read_mode.close()

    dosya.close()

    sleep(5)
    chrome_driver.close()


kitap_bilgilerini_topla() 
