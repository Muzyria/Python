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
time.sleep(1)


# Удаление автомобилей
# lst_car = ['S101500002110180' + str(i) for i in range(70, 91)]
id_car_start = 'S101500002110180'  #  without two simbol
for i in range(70, 91):
    new_id = f'{id_car_start}{i}'
    print(new_id + ' will deleted')

    # Ищем машинку и нажимем на нее
    try:
        action = ActionChains(driver)
        car = driver.find_element(By.XPATH, f'//*[text()="{new_id}"]')
        action.move_to_element(car).perform()
        time.sleep(2)
        car.click()
        print(f'Click {new_id} car')
        time.sleep(2)
        # Нажимаем удалить девайс
        button_remove_device = driver.find_element(By.XPATH, '//*[text()="Remove Device"]')
        button_remove_device.click()
        time.sleep(3)
    except Exception:
        print(f'Не найден {new_id}')




driver.close()
