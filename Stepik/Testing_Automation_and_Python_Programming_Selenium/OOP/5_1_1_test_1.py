import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class NoTest1:

    def select_product(self):
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        s = Service(r'C:\Git_Muzyria\Python\Stepik\Testing_Automation_and_Python_Programming_Selenium\OOP\resource'
                    r'\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(2)

        print('Start test')

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


test = NoTest1()
test.select_product()

