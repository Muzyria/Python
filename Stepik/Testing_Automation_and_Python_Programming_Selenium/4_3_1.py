import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# s = Service(r'C:\Git_Muzyria\Python\Python\Stepik\Testing_Automation_and_Python_Programming_Selenium\chromedriver.exe')  # win
s = Service()  # linux
driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/')
driver.maximize_window()

# user_name = driver.find_element(By.ID, "user-name")  # ID
# user_name = driver.find_element(By.NAME, "user-name")  # NAME
user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')  # XPATCH

user_name.send_keys("standart_user")

time.sleep(3)
driver.close()
