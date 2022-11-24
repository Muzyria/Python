import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'C:\Git_Muzyria\Python\Python\Stepik\Testing_Automation_and_Python_Programming_Selenium\chromedriver.exe')
driver = webdriver.Chrome(service=s)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')  # id XPATH
user_name.send_keys(login_standard_user)
print('Input Login')
# time.sleep(2)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(2)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(2)
# user_name.send_keys('er')

password = driver.find_element(By.XPATH, '//input[@id="password"]')  # id XPATH
password.send_keys(password_all)
print('Input Password')
password.send_keys(Keys.RETURN)

# password = driver.find_element(By.XPATH, '//input[@id="password"]')  # id XPATH
# password.send_keys(password_all)
# print('Input Password')
#
# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")  # id XPATH
# button_login.click()
# print('Click Login Button')

filter_1 = driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
filter_1.click()
print('Click filter_1')
time.sleep(2)
filter_1.send_keys(Keys.DOWN)
time.sleep(2)
filter_1.send_keys(Keys.RETURN)


time.sleep(2)
driver.close()
