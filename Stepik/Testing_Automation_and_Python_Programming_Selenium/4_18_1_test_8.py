import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'C:\Git_Muzyria\Python\Python\Stepik\Testing_Automation_and_Python_Programming_Selenium\chromedriver.exe')
driver = webdriver.Chrome(service=s)

base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.maximize_window()

check_box = driver.find_element(By.XPATH, '//button[@aria-label="Toggle"]')
check_box.click()


time.sleep(2)
driver.close()
