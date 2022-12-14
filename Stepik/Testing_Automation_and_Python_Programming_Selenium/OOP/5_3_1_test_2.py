import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from login_page import Login_page


class NoTest2:

    def select_product(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(2)

        print('Start test')

        login_standard_user = "performance_glitch_user"
        password_all = "secret_sauce"

        login = Login_page(driver)
        login.authorization(login_name=login_standard_user, login_password=password_all)

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')))
        select_product.click()
        print('Click Select Product')
        time.sleep(2)

        enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="shopping_cart_link"]')))
        enter_shopping_cart.click()
        print('Click Enter Shopping Cart')
        time.sleep(2)

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]')))
        value_success_test = success_test.text
        print(value_success_test)
        assert value_success_test == 'YOUR CART'
        print('Test Succcess !!!')


test = NoTest2()
test.select_product()

