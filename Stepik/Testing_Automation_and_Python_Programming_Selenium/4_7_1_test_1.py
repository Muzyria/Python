import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'C:\Git_Muzyria\Python\Python\Stepik\Testing_Automation_and_Python_Programming_Selenium\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://www.saucedemo.com/')
driver.maximize_window()

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')  # id XPATH
user_name.send_keys("standard_user")

password = driver.find_element(By.XPATH, '//input[@id="password"]')  # id XPATH
password.send_keys("secret_sauce")

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")  # id XPATH
button_login.click()

time.sleep(3)
driver.close()
