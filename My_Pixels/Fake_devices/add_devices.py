import time
import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'C:\Git_Muzyria\Python\Python\My_Pixels\driver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
# driver.implicitly_wait(20)

base_url = 'https://control.syncwise360.com/#login'
driver.get(base_url)
driver.maximize_window()
time.sleep(5)

login_standard_user = input('Enter User Login -> ')  # Enter login
# login_standard_user = ''  # Закомитить это
password_all = login_standard_user

user_name = driver.find_element(By.XPATH, '//input[@id="username"]')  # id XPATH
user_name.send_keys(login_standard_user)
print('Input Login')

password = driver.find_element(By.XPATH, '//input[@id="password"]')  # id XPATH
password.send_keys(password_all)
print('Input Password')

button_login = driver.find_element(By.XPATH, '//button[@id="btn-submit"]')  # id XPATH
button_login.click()
print('Click Login Button')

time.sleep(2)

input_search = driver.find_element(By.XPATH, '//input[@class="search"]')
input_search.send_keys('salt')
input_search.send_keys(Keys.RETURN)
print('input search')
time.sleep(1)

result_salt = driver.find_element(By.XPATH, '//*[text()="Salt Creek Golf Club"]')
result_salt.click()
print('Click result')
time.sleep(3)


# Добавление новых автомобилей
id_car_start = 'S101500002110180'  #  without two simbol
for i in range(70, 91):
    new_id = f'{id_car_start}{i}'
    print(new_id + ' will added')

    # Нажатие на кнопку ADD
    action = ActionChains(driver)
    add_new_car = driver.find_element(By.XPATH, '//th[@class="bt control add"]')
    # add_new_car = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/section/div[3]/div[5]/table[1]/thead/tr/th[5]')
    action.move_to_element(add_new_car).perform()
    time.sleep(2)
    add_new_car.click()
    print('Click add new car')
    time.sleep(2)

    # Нажимаем на выпадающий список
    select_devise_model = driver.find_element(By.XPATH, '//select[@name="id_deviceModel"]')
    select_devise_model.click()
    time.sleep(2)

    # Выбираем YTR
    select_devise_model_YTR = driver.find_element(By.XPATH, '//option[text()="Utility Tablet - YTR"]')
    select_devise_model_YTR.click()
    time.sleep(2)

    # Вставляем номер машинки
    input_id_device = driver.find_element(By.XPATH, '//input[@name="id_device"]')
    input_id_device.send_keys(new_id)
    time.sleep(1)

    # Вставляем имя машинки
    input_name_device = driver.find_element(By.XPATH, '//input[@name="cartName"]')
    input_name_device.send_keys(new_id[-2::])
    time.sleep(1)

    # Нажимаем кнопку SAVE
    button_save = driver.find_element(By.XPATH, '//*[text()="Save"]')
    button_save.click()
    time.sleep(10)

    # # Перезагружаем
    # driver.refresh()
    # time.sleep(4)


time.sleep(2)
driver.close()
