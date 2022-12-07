import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Приветствие и выбор товара
print('Приветствую тебя в нашем интеренет магазине')
print('Выбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light,'
      ' 3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie,'
      ' 6 - Test.allTheThings() T-Shirt (Red)')
product = int(input())

locators = {1: {'name_product': '//a[@id="item_4_title_link"]',
                'price_product': '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div',
                'button_product': '//button[@id="add-to-cart-sauce-labs-backpack"]'},
            2: {'name_product': '//a[@id="item_0_title_link"]',
                'price_product': '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div',
                'button_product': '//button[@id="add-to-cart-sauce-labs-backpack"]'},
            3: {'name_product': '//a[@id="item_1_title_link"]',
                'price_product': '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div',
                'button_product': '//button[@id="add-to-cart-sauce-labs-backpack"]'},
            4: {'name_product': '//a[@id="item_5_title_link"]',
                'price_product': '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div',
                'button_product': '//button[@id="add-to-cart-sauce-labs-backpack"]'},
            5: {'name_product': '//a[@id="item_2_title_link"]',
                'price_product': '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div',
                'button_product': '//button[@id="add-to-cart-sauce-labs-backpack"]'},
            6: {'name_product': '//a[@id="item_3_title_link"]',
                'price_product': '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div',
                'button_product': '//button[@id="add-to-cart-sauce-labs-backpack"]'}}

s = Service(r'C:\Git_Muzyria\Python\Stepik\Testing_Automation_and_Python_Programming_Selenium\chromedriver.exe')
driver = webdriver.Chrome(service=s)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

# Авторизация на сайте
user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')  # id XPATH
user_name.send_keys(login_standard_user)
print('Input Login')
password = driver.find_element(By.XPATH, '//input[@id="password"]')  # id XPATH
password.send_keys(password_all)
print('Input Password')
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")  # id XPATH
button_login.click()
print('Click Login Button')

# Выбираем продукт
"""INFO product #1"""
# Название продукта
# product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
product_1 = driver.find_element(By.XPATH, locators[product]['name_product'])

value_product_1 = product_1.text
print(value_product_1)

# Цена продукта
price_product_1 = driver.find_element(By.XPATH, locators[product]['price_product'])
value_price_product_1 = price_product_1.text
print(value_price_product_1)

# Нажатие на кнопку (Добавления в корзину)
select_price_product_1 = driver.find_element(By.XPATH, locators[product]['button_product'])
select_price_product_1.click()
print('Select Product 1')

# Входим в корзину
cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
cart.click()
print('Enter cart')

"""INFO Cart Product 1"""
cart_product_1 = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print('INFO Cart Product 1 GOOD')

price_cart_product_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print('INFO Cart Price Product 1 GOOD')

# Нажимаем кнопку Checkout в корзине
checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout.click()
print('Click Checkout')

# Оформление заказа заполняем поля клиента
"""Select User INFO"""
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys('Alex')
print('Input First Name')
second_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
second_name.send_keys('Ivanov')
print('Input Second Name')
postal_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
postal_code.send_keys('1234')
print('Input Postal Code')

# Нажимеаем кнопку Continue
button_continue = driver.find_element(By.XPATH, '//input[@id="continue"]')
button_continue.click()
print('Click Button Continue')

# Провекрка заказа
"""INFO Finish Product 1"""
finish_product_1 = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print('INFO Finish Product 1 GOOD')

price_finish_product_1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_cart_price_product_1 == value_finish_price_product_1
print('INFO Finish Price Product 1 GOOD')

summery_price = driver.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]')
value_summery_price = summery_price.text
print(value_summery_price)
item_total = 'Item total: ' + value_finish_price_product_1
print(item_total)
assert value_summery_price == item_total
print('Total Summary price GOOD')

# Нажимаем кнопку Finish
finish_button = driver.find_element(By.XPATH, '//button[@id="finish"]')
finish_button.click()
print('Click Finish Button')

time.sleep(3)
driver.close()
