from datetime import datetime, timedelta
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'C:\Git_Muzyria\Python\Python\Stepik\Testing_Automation_and_Python_Programming_Selenium\chromedriver.exe')
driver = webdriver.Chrome(service=s)

base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

# Находим поле календаря
new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
print(new_date.get_attribute('value'))  # Выводим текущую дату
new_date.click()  # Кликаем по полю календаря
[new_date.send_keys(Keys.BACKSPACE) for _ in range(10)]  # Стираем поле календаря
time.sleep(2)

#  Заполняем поле календаря новыми данными
[new_date.send_keys(i) for i in str((datetime.now() + timedelta(days=10)).strftime('%d/%m/%Y'))]
time.sleep(2)
new_date.send_keys(Keys.RETURN)
print(new_date.get_attribute('value'))  # Выводим новую дату

time.sleep(3)
driver.close()
