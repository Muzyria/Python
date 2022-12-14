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
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(1)

        print('Start test')

        lst_login_user = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
        password_all = "secret_sauce"

        for login in lst_login_user:
            try:
                user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
                user_name.send_keys(login)
                print('Input Login')

                password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
                password.send_keys(password_all)
                print('Input Password')

                button_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
                button_login.click()
                print('Click Login Button')
                time.sleep(2)



                success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]')))
                value_success_test = success_test.text
                print(value_success_test)
                assert value_success_test == 'PRODUCTS'
                print('Test Succcess !!!')

                button_menu = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
                button_menu.click()
                print('Click Button Menu')
                time.sleep(1)

                items_logout = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="logout_sidebar_link"]')))
                items_logout.click()
                print('Click Item Logout')
                time.sleep(2)
            except Exception:
                print('Error ---------------------------------')

test = NoTest1()
test.select_product()

