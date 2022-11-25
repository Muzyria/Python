import time
import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'C:\Git_Muzyria\Python\Python\My_Pixels\driver\chromedriver.exe')
driver = webdriver.Chrome(service=s)

base_url = 'https://control.syncwise360.com/#login'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

login_standard_user = "superadmin"
password_all = "superadmin"

user_name = driver.find_element(By.XPATH, '//input[@id="username"]')  # id XPATH
user_name.send_keys(login_standard_user)
print('Input Login')

password = driver.find_element(By.XPATH, '//input[@id="password"]')  # id XPATH
password.send_keys(password_all)
print('Input Password')

button_login = driver.find_element(By.XPATH, '//button[@id="btn-submit"]')  # id XPATH
button_login.click()
print('Click Login Button')

time.sleep(3)

input_search = driver.find_element(By.XPATH, '//input[@class="search"]')
input_search.send_keys('salt')
input_search.send_keys(Keys.RETURN)
print('input search')
time.sleep(3)




# driver.execute_script('window.scrollTo(0, 500)')
# time.sleep(2)
# time.sleep(2)
#
# action = ActionChains(driver)
# red_t_shirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
# action.move_to_element(red_t_shirt).perform()
# time.sleep(2)


time.sleep(2)
driver.close()
