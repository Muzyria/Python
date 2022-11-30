import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'C:\Git_Muzyria\Python\Python\Stepik\Testing_Automation_and_Python_Programming_Selenium\chromedriver.exe')
driver = webdriver.Chrome(service=s)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
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

"""INFO product #1"""
product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_price_product_1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
select_price_product_1.click()
print('Select Product 1')

cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
cart.click()
print('Enter cart')

"""INFO Cart Product 1"""
cart_product_1 = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
value_cart_product_1 = cart_product_1.text
print(value_product_1)
assert value_product_1 == value_cart_product_1
print('INFO Cart Product 1 GOOD')

price_cart_product_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print('INFO Cart Price Product 1 GOOD')

time.sleep(2)
driver.close()
