import random
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

        result_salt = self.driver.find_element(By.XPATH, '//*[text()="MGI Golf"]')
        result_salt.click()
        print('Click result')
        time.sleep(1)

    def manage_devise_click(self):
        manage_button = self.driver.find_element(By.CSS_SELECTOR, 'section[class="horizontal-box stretched-box"] div[class="i"]:nth-child(4)')
        manage_button.click()
        print('Click Manage Device')
        time.sleep(1)

    def display_all_click(self):
        display_all_button = self.driver.find_element(By.CSS_SELECTOR, 'th[class="bt display-all"]')
        display_all_button.click()
        print('Click display_all')
        time.sleep(5)

    def all_list(self):
        table = self.driver.find_elements(By.CSS_SELECTOR, 'table[class="style4 center company-devices-tbl"] tbody tr')

        # list_all_check_boxes = [item for item in table]
        # random.shuffle(list_all_check_boxes)
        #
        # for number, item in enumerate(list_all_check_boxes, 1):
        #     name_item = item.text.split(" ")[0]
        #     print(f'{name_item} Clicked ---> {number}')
        #     try:
        #         item.find_element(By.CSS_SELECTOR, 'input').click()
        #         time.sleep(5)
        #
        #         # item.find_element(By.CSS_SELECTOR, 'input')
        #         # self.driver.execute_script("arguments[0].scrollIntoView();", item)
        #         # element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input')))
        #         # element.click()
        #         # item.find_element(By.CSS_SELECTOR, 'input').click()
        #     except Exception:
        #         print(f"Ошибка: при попытке --- {number}")
        #         break

        for number, item in enumerate(table, 1):
            name_item = item.text.split(" ")[0]
            print(f'{name_item} Clicked ---> {number}')
            try:
                item.find_element(By.CSS_SELECTOR, 'input').click()
            except Exception:
                print(f"Ошибка: при попытке --- {number}")
                break


        time.sleep(300)




test = TestCheckBox()
test.run()
test.login()
test.search('mgi ')

test.manage_devise_click()
test.display_all_click()

test.all_list()

time.sleep(5)

test.driver.close()