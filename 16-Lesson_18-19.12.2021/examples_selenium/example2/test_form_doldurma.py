from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver_path = "/home/muratcabuk/chromedriver"


@pytest.fixture
def chrome_driver():
    chrome_driver = webdriver.Chrome(executable_path=driver_path)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_formu_doldur_gonder(chrome_driver):

    chrome_driver.get("https://demoqa.com/automation-practice-form")
    print("Açılan sayfanın adı : " + chrome_driver.title)


    chrome_driver.find_element(By.ID, "firstName").click()
    chrome_driver.find_element(By.ID, "firstName").send_keys("Murat")
    sleep(1)

    chrome_driver.find_element(By.ID, "lastName").click()
    chrome_driver.find_element(By.ID, "lastName").send_keys("Cabuk")
    sleep(1)

    chrome_driver.find_element(By.ID, "userEmail").click()
    chrome_driver.find_element(By.ID, "userEmail").send_keys("murat@cabuk.com")
    sleep(1)


    # chrome_driver.find_element(By.ID, "gender-radio-1").click()
    chrome_driver.find_element(By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]').click()
    sleep(1)

    chrome_driver.find_element(By.ID, "userNumber").click()
    chrome_driver.find_element(By.ID, "userNumber").send_keys("3456786234")
    sleep(1)

    # dateofbirth temizlerdiğinde fom siliniyor bu nedenle olduğu gibi kabül edilecek

    #chrome_driver.find_element(By.ID, "dateOfBirthInput").clear()
    #chrome_driver.find_element(By.ID, "dateOfBirthInput").click()
    #chrome_driver.find_element(By.ID, "dateOfBirthInput").send_keys(Keys.CONTROL + "a")
    #chrome_driver.find_element(By.ID, "dateOfBirthInput").send_keys(Keys.DELETE)
    #chrome_driver.find_element(By.ID, "dateOfBirthInput").send_keys("13 Jan 1980")
    #sleep(1)

    chrome_driver.find_element(By.ID, "subjectsInput").click()
    chrome_driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
    chrome_driver.find_element(By.ID, "subjectsInput").send_keys(Keys.RETURN)
    sleep(1)

    # chrome_driver.find_element(By.ID, "hobbies-checkbox-2").click()
    # //*[@id="hobbiesWrapper"]/div[2]/div[1]
    chrome_driver.find_element(By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[1]').click()
    sleep(1)

    chrome_driver.find_element(By.ID, "uploadPicture").send_keys("/home/muratcabuk/a.jpg")
    sleep(1)

    chrome_driver.find_element(By.ID, "currentAddress").click()
    chrome_driver.find_element(By.ID, "currentAddress").send_keys("bu benim adresim")
    sleep(1)

    chrome_driver.find_element(By.CLASS_NAME, "css-yk16xz-control").click()
    sleep(1)

    # state dropbox
    a = chrome_driver.find_element(By.XPATH, '//*[@id="state"]/div')
    
    
    a.click()
    sleep(1)

    #aa = chrome_driver.find_element(By.ID, "react-select-3-option-1")  # developer modda click eventlerini yakalayarak bulduk
    aa = chrome_driver.find_element(By.XPATH, '//*[@id="react-select-3-option-1"]')    
    chrome_driver.execute_script("arguments[0].click();", aa)
    
    #action_state=ActionChains(chrome_driver) # action da hata verdi
    #action_state.move_to_element(aa).click().perform()

    #aa.click() # doğrudan click leyince hata veriyor


    sleep(1)

    # city dropbox
    b = chrome_driver.find_element(By.XPATH, '//*[@id="city"]/div')
    b.click()

    ##bb = chrome_driver.find_element(By.ID, "react-select-4-option-0") # developer modda click eventlerini yakalayarak bulduk
    bb = chrome_driver.find_element(By.XPATH, '//*[@id="react-select-4-option-1"]')    
    chrome_driver.execute_script("arguments[0].click();", bb)




    sleep(1)

    chrome_driver.find_element(By.ID, "submit").click()
    sleep(2)

    mesaj = chrome_driver.find_element(By.ID,"example-modal-sizes-title-lg").text
    print(mesaj)

    if mesaj != "Thanks for submitting the form":  # beklenen mesa değiştirilip hata durumuda gorulebilir
        raise Exception("form işlemleri başarısız")
    sleep(2)