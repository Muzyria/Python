import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service(r'C:\Git_Muzyria\Python\Stepik\Testing_Automation_and_Python_Programming_Selenium\chromedriver.exe')
driver = webdriver.Chrome(service=s)

base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()

print('start test')
button_enabled_after = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '//button[@id="enableAfter"]')))
button_enabled_after.click()
print('click button')

print('start test 2')
button_visible_after = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '//button[@id="visibleAfter"]')))
button_visible_after.click()
print('click button 2')

time.sleep(2)
driver.close()
