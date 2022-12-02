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
print(new_date.get_attribute('value'))
new_date.click()  # Кликаем по полю календаря
[new_date.send_keys(Keys.BACKSPACE) for _ in range(10)]  # Стираем поле календаря
time.sleep(2)

new_date.send_keys(datetime.now() + timedelta(days=10))
time.sleep(2)
new_date.send_keys(Keys.RETURN)
print(new_date.get_attribute('value'))


# new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
# new_date.click()
# time.sleep(2)
#
# now_date = datetime.datetime.utcnow().strftime("%d")
# print(now_date)
# date = int(now_date) + 1
# locator = f'//div[@aria-label="Choose Saturday, December {str(date)}rd, 2022"]'
# print(locator)
#
# date_3 = driver.find_element(By.XPATH, locator)
# # date_today = driver.find_element(By.XPATH, '//div[contains(@class, "react-datepicker__day--today")]')
# date_3.click()
# print(new_date.get_attribute('value'))


time.sleep(3)
driver.close()
