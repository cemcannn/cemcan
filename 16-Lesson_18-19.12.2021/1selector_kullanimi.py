################################################################ ID

# "<html>
#  <body>
#   <form id="loginForm">
#    <input name="username" type="text" />
#    <input name="password" type="password" />
#    <input name="continue" type="submit" value="Login" />
#   </form>
#  </body>
# </html>"

# login_form = driver.find_element_by_id("loginForm")

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver_path = "/home/muratcabuk/chromedriver"
chrome_driver = webdriver.Chrome(executable_path=driver_path)
chrome_driver.get("https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Banka+Hakkinda/Iletisim/Subeler")

selected_id = "search-query"

search_input_element = chrome_driver.find_element_by_id(selected_id)

# diğer kullanım için link : https://selenium-python.readthedocs.io/locating-elements.html
search_input_element = chrome_driver.find_element(By.ID, selected_id)

print("ID selector :" + search_input_element.get_attribute("name"))

sleep(1)



################################################################ NAME

# "<html>
#  <body>
#   <form id="loginForm">
#    <input name="username" type="text" />
#    <input name="password" type="password" />
#    <input name="continue" type="submit" value="Login" />
#   </form>
#  </body>
# </html>"

# login_form = driver.find_element_by_name("username")

chrome_driver.get("https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Banka+Hakkinda/Iletisim/Subeler")

selected_name = "search-query"

search_input_element = chrome_driver.find_element_by_name(selected_name)

# diğer kullanım için link : https://selenium-python.readthedocs.io/locating-elements.html
search_input_element = chrome_driver.find_element(By.NAME, selected_name)

print("NAME selector :" +search_input_element.get_attribute("id"))

sleep(1)


################################################################ CLASS

# "<html>
#  <body>
#   <p class="content">Site content goes here.</p>
# </body>
# </html>"

# login_form = driver.find_element_by_class("username")

chrome_driver.get("https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Banka+Hakkinda/Iletisim/Subeler")

selected_class = "nav-mega-menu"

research_div = chrome_driver.find_element_by_class_name(selected_class)

# diğer kullanım için link : https://selenium-python.readthedocs.io/locating-elements.html
research_div = chrome_driver.find_element(By.CLASS_NAME, selected_class)

# print("CLASS selector :" +research_div.get_attribute('innerHTML'))
print("CLASS selector :" +research_div.get_attribute('id'))


sleep(1)




################################################################ CSS

# "<html>
#  <body>
#   <p class="content">Site content goes here.</p>
# </body>
# </html>"

# login_form = driver.find_element_by_class("username")

chrome_driver.get("https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Banka+Hakkinda/Iletisim/Subeler")

selected_class = "div[class='research nav-mega-menu']"

research_div = chrome_driver.find_element_by_css_selector(selected_class)

# diğer kullanım için link : https://selenium-python.readthedocs.io/locating-elements.html
research_div = chrome_driver.find_element(By.CSS_SELECTOR, selected_class)

# print("CSS selector :" + research_div.get_attribute('innerHTML'))

print("CSS selector :" + research_div.get_attribute('id'))

sleep(1)



################################################################ XPATH

# Bazı temel XPath ifadeleri:
#
# - Xpath=//input[@type='text']
# - Xpath= //label[@id='lblhata′]
# - Xpath= //input[@value=Gönder]
# - Xpath=//*[@class='border-red']
# - Xpath=//a[@href='/anasayfa']
# - Xpath= //img[@src='//https://images.abc.com/10/5.png']

chrome_driver.get("https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Banka+Hakkinda/Iletisim/Subeler")

selected_xpath = "//div[@class='research nav-mega-menu']"
# //div[@class='research nav-mega-menu']
# //*[@id="research"]
# /html/body/header/nav/div[3]/div[4]

research_div = chrome_driver.find_element_by_xpath(selected_xpath)

# diğer kullanım için link : https://selenium-python.readthedocs.io/locating-elements.html
research_div = chrome_driver.find_element(By.XPATH, selected_xpath)

# print("XPATH selector :" + research_div.get_attribute('innerHTML'))
print("XPATH selector :" + research_div.get_attribute('id'))
sleep(5)
chrome_driver.close()