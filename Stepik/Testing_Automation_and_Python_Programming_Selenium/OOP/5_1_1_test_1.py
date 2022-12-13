import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class NoTest1:

    def select_product(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # s = Service(r'C:\Git_Muzyria\Python\Stepik\Testing_Automation_and_Python_Programming_Selenium\OOP\resource'
        #             r'\chromedriver.exe')
        # driver = webdriver.Chrome(service=s)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(2)

        print('Start test')

        login_standard_user = "standard_user"
        password_all = "secret_sauce"

        user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
        user_name.send_keys(login_standard_user)
        print('Input Login')

        password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password.send_keys(password_all)
        print('Input Password')

        button_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        button_login.click()
        print('Click Login Button')
        time.sleep(2)

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
        assert


test = NoTest1()
test.select_product()

