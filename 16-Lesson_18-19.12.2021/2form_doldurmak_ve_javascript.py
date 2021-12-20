# https://selenium-python.readthedocs.io/navigating.html#filling-in-forms

###########################3333 inputbox

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select  # html select element için gerekli

from time import sleep

driver_path = "/home/muratcabuk/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.google.com/")


inputbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')

inputbox = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')

sleep(5)

inputbox.send_keys("Türkiye")

sleep(2)

#################################33 checkbox

checkbox = driver.find_element_by_id('hobi_sinema')
checkbox.click()


######### checkbox seçilimi kontrolu
## is_selected
hobi_sinema_is_selected = driver.find_element_by_id('hobi_sinema').is_selected()

# checked
hobi_sinema_is_selected = driver.find_element_by_id('hobi_sinema').get_attribute("checked")


#################################33 radiobutton

driver.find_element_by_id('my_radiobutton').click()

pageSize_5_boolean = driver.find_element_by_id('my_radiobutton').is_selected()

pageSize_5_other = driver.find_element_by_id('my_radiobutton').get_attribute("checked")


#####################################333 dropdown - select element

# <td>
#     <select id="search_grade">
#         <option selected>(no value)</option>
#         <option value="K">K</option>
#         <option value="1">1</option>
#         <option value="2">2</option>
#         <option value="3">3</option>
#         <option value="4">4</option>
#         <option value="5">beş</option>
#     </select>
# </td>

grade_dropdown = Select(driver.find_element_by_id("search_grade"))

grade_dropdown.select_by_index(6)
grade_dropdown.select_by_value("5")
grade_dropdown.select_by_visible_text("beş")

# 1. .all_selected_options — Get the list of all the selected options.
# 2. .first_selected_option — Return the first option that has been selected from the dropdown and unlike the above method it would return a single web element, not a list.
# 3. .is_multiple — Return True if the dropdown allows multi-selection and return NoneType otherwise.
# 4. .options — Get a list of all available options in a dropdown.

########################################3 button click
driver.find_element_by_id("search").click()

#######################################333 link kullanımı

# doğrudan linke tıklamak
driver.find_element_by_id("a_link").click()

# url e gitmek
privacy_object = driver.find_element_by_id("a_link")
privacy_link = privacy_object.get_attribute("href")
driver.get(privacy_link)

############################################3  javascript çalıştırmak

javaScript = "document.getElementsByName('username')[0].click();"
driver.execute_script(javaScript)

## mesela sayfanızda herhangibir elementin
# backgroud-color unu değiştiren change() adında bir javascirpt fonksiyonunuz olsun

driver.execute_script("change()")

#### ###################################### javascript den değer okumak

my_innerText = driver.execute_script('return document.getElementById("my_div").innerText')
print (my_innerText)

##############################################3 cookie

# Go to the correct domain
driver.get("http://www.example.com")

# Now set the cookie. This one's valid for the entire domain
cookie = {'name' : 'foo', 'value' : 'bar'}
driver.add_cookie(cookie)

# And now output all the available cookies for the current URL
mylist = driver.get_cookies()













driver.close()