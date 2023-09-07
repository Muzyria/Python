
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


class TestCheckBox:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def run(self):
        base_url = 'https://dev-control.syncwise360.com/#login'
        self.driver.get(base_url)
        self.driver.maximize_window()
        time.sleep(2)
        print('Start test')

    def login(self):
        user_name = self.driver.find_element(By.XPATH, '//input[@id="username"]')  # id XPATH
        user_name.send_keys('superadmin')
        print('Input Login')

        password = self.driver.find_element(By.XPATH, '//input[@id="password"]')  # id XPATH
        password.send_keys('superadmin')
        print('Input Password')

        button_login = self.driver.find_element(By.XPATH, '//button[@id="btn-submit"]')  # id XPATH
        button_login.click()
        print('Click Login Button')

        time.sleep(2)

    def search(self, data):
        input_search = self.driver.find_element(By.XPATH, '//input[@class="search"]')
        input_search.send_keys(data)
        input_search.send_keys(Keys.RETURN)
        print(f'input search --- {data}')
        time.sleep(1)

        # result_salt = self.driver.find_element(By.XPATH, '//*[text()="Salt Creek Golf Club"]')
        # result_salt.click()
        # print('Click result')
        # time.sleep(3)


test = TestCheckBox()
test.run()
test.login()
test.search('mgi ')

time.sleep(5)

test.driver.close()