import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'C:\Git_Muzyria\Stepik\Testing_Automation_and_Python_Programming_Selenium\chromedriver.exe')
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

"""INFO product #2"""
product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
value_price_product_2 = price_product_2.text
print(value_price_product_2)

select_price_product_2 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
select_price_product_2.click()
print('Select Product 2')

cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
cart.click()
print('Enter cart')

"""INFO Cart Product 1"""
cart_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print('INFO Cart Product 1 GOOD')

price_cart_product_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print('INFO Cart Price Product 1 GOOD')

"""INFO Cart Product 2"""
cart_product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_2 == value_cart_product_2
print('INFO Cart Product 2 GOOD')

price_cart_product_2 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_cart_price_product_2 = price_cart_product_2.text
print(value_cart_price_product_2)
assert value_price_product_2 == value_cart_price_product_2
print('INFO Cart Price Product 2 GOOD')

checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout.click()
print('Click Checkout')

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

button_continue = driver.find_element(By.XPATH, '//input[@id="continue"]')
button_continue.click()
print('Click Button Continue')

"""INFO Finish Product 1"""
finish_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_cart_product_1 == value_finish_product_1
print('INFO Finish Product 1 GOOD')

price_finish_product_1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_cart_price_product_1 == value_finish_price_product_1
print('INFO Finish Price Product 1 GOOD')

"""INFO Finish Product 2"""
finish_product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_cart_product_2 == value_finish_product_2
print('INFO Finish Product 2 GOOD')

price_finish_product_2 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_finish_price_product_2 = price_finish_product_2.text
print(value_finish_price_product_2)
assert value_cart_price_product_2 == value_finish_price_product_2
print('INFO Finish Price Product 2 GOOD')


summery_price = driver.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]')
value_summery_price = summery_price.text
print(value_summery_price)
sum_price_product = float(value_finish_price_product_1.replace('$', '')) + float(value_finish_price_product_2.replace('$', ''))
item_total = 'Item total: ' + '$' + str(sum_price_product)
print(item_total)
assert value_summery_price == item_total
print('Total Summary price GOOD')

finish_button = driver.find_element(By.XPATH, '//button[@id="finish"]')
finish_button.click()
print('Click Finish Button')

time.sleep(3)
driver.close()
