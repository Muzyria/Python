import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'C:\Git_Muzyria\Python\Python\Stepik\Testing_Automation_and_Python_Programming_Selenium\chromedriver.exe')
driver = webdriver.Chrome(service=s)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_use"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')  # id XPATH
user_name.send_keys(login_standard_user)
print('Input Login')

password = driver.find_element(By.XPATH, '//input[@id="password"]')  # id XPATH
password.send_keys(password_all)
print('Input Password')

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")  # id XPATH
button_login.click()
print('Click Login Button')

warring_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
value_warring_text = warring_text.text

assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
print('Good test')

time.sleep(2)
driver.close()
