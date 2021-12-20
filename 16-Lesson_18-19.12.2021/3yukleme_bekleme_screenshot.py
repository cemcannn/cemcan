# 1. Yöntem: element click yapalabilir duruma gelinceye kadar beklemek / wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select  # html select element için gerekli
import time

driver_path = "/home/muratcabuk/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.google.com/")

driver.find_element(By.ID, "search").click()
time.sleep(3)  # sayfa 1 sn sonra yüklenmiş bile olsa yine de 3 sn bekler
table = driver.find_element(By.XPATH,'//*[@id="results"]/table')

# ancak böyle beklemek çok mantıklı olmayabilir.
# Çünki 3sn nin de garantisi yok. gerektiği kadar beklemek için alttaki kod
# bloğu kullanılabilir.Buna **explicit wait** deniyor.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.find_element(By.ID,"search").click()

# maksimum 10 sn bekle demek oluyor.
table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "resulttable")))
# same as the set up chunk of code

# - ayrıca alttakilerde kullanılabilir.
# - title_is
# - title_contains
# - presence_of_element_located
# - visibility_of_element_located
# - visibility_of
# - presence_of_all_elements_located
# - text_to_be_present_in_element
# - text_to_be_present_in_element_value
# - frame_to_be_available_and_switch_to_it
# - invisibility_of_element_located
# - element_to_be_clickable
# - staleness_of
# - element_to_be_selected
# - element_located_to_be_selected
# - element_selection_state_to_be
# - element_located_selection_state_to_be
# - alert_is_present


# ###################################2. Yöntem: Scroll until on-screen / Scroll until on-screen

driver.find_element_by_id("search").click()
time.sleep(5)
# scroll to a certain height
driver.execute_script("window.scrollTo(0, 5000)")
# scroll to the bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
# same as the last chunk of code

#################################3. yontem javascript çalıştırmak

# same as the set up chunk of code
...
driver.implicitly_wait(10)
form_url = "https://iqssdss2020.pythonanywhere.com/tutorial/formhidden/search"
# same as the set up chunk of code
...
driver.execute_script(f'document.getElementById("search").click();')
# same as the set up chunk of code

######################## **4. Yöntem: yapılamsı gereken öcelikli işlerin yapılması** ActionChain : https://selenium-python.readthedocs.io/api.html?highlight=ActionChains#module-selenium.webdriver.common.action_chains

# Örneğin ilgili elentin ortya çıkması için başka bir element üzerinde mouse hover yaparak 1 sn beklemek gerekebilir. Yada bir butona bastıkta sonra ajax ile birlikte veriler yükleniyor olabilir.
# Mesela akttaki kodda ilgili tag in üzerine actionchain iile mouse u gotürüp ilgili elenmtim görünmesini sağlıyoruz.


# same as the set up chunk of code
...
from selenium.webdriver.common.action_chains import ActionChains

# same as the set up chunk of code
...
driver.implicitly_wait(10)
# same as the set up chunk of code
...
name_tag = driver.find_element_by_tag_name("span")
hov = ActionChains(driver).move_to_element(name_tag)
# action ı oluşturuyoruz ve alttaki perform fonksiyonu ile çalıştırıoruz.


hov.perform()
hov_id = name_tag.get_attribute("aria-describedby")
print(hov_id)
hov_text = driver.find_element_by_id(hov_id).text
print(hov_text)


######################################################3 screenshot

from selenium import webdriver
from time import sleep

driver_path = "/home/muratcabuk/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

try:
    driver.get("https://www.python.org")
    sleep(1)
except:
    driver.get_screenshot_as_file("screenshot.png")
finally:
    driver.quit()








