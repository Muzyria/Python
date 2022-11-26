import time
import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'C:\Git_Muzyria\Python\Python\My_Pixels\driver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(20)

base_url = 'https://control.syncwise360.com/#login'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

login_standard_user = ""
password_all = ""

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


id_car_start = 'S101500002110180'  #  without two simbol
for i in range(70, 91):
    new_id = f'{id_car_start}{i}'
    print(new_id)

    action = ActionChains(driver)
    add_new_car = driver.find_element(By.XPATH,
                                      '//*[@id="workarea"]/div[2]/section/div[3]/div[5]/table[3]/thead/tr/th[4]')
    action.move_to_element(add_new_car).perform()
    add_new_car.click()
    print('Click add new car')
    time.sleep(2)

    select_devise_model = driver.find_element(By.XPATH, '//select[@name="id_deviceModel"]')
    select_devise_model.click()
    time.sleep(2)

    select_devise_model_YTR = driver.find_element(By.XPATH, '//option[text()="Utility Tablet - YTR"]')
    select_devise_model_YTR.click()
    time.sleep(2)

    driver.refresh()
    time.sleep(4)



# driver.execute_script('window.scrollTo(0, 500)')
# time.sleep(2)
# time.sleep(2)
#
# action = ActionChains(driver)
# red_t_shirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
# action.move_to_element(red_t_shirt).perform()
# time.sleep(2)


time.sleep(2)
driver.close()
