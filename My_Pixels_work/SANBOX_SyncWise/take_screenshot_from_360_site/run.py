
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class NoTest:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login_site(self):
        """login site and enter"""
        base_url = 'https://sandbox.syncwise360.com/login'
        self.driver.get(base_url)
        self.driver.maximize_window()
        time.sleep(2)

        print('Start test')

        login_standard_user = "igorperetssuperior"
        password_all = "Qwerty01!"

        # LOGIN PAGE
        # INPUT LOGIN
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#username')))
        user_name.send_keys(login_standard_user)
        print('Input Login')

        # INPUT PASSWORD
        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#password')))
        password.send_keys(password_all)
        print('Input Password')

        # CLICK LOGIN BUTTON
        button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="submit"]')))
        button_login.click()
        print('Click Login Button')
        time.sleep(10)

    def take_picture(self):
        # CLICK
        nav_yama = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="number" and text()="49"]')))
        nav_yama.click()
        print('Click Car Button')
        time.sleep(5)

        print('Try move slider')
        # slider_input = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ng-scroll-content')))
        slider_input = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[@class="blank_hole" and text()="9"]')))
        # slider_input.click()



        action = ActionChains(self.driver)
        action.move_to_element(slider_input).perform()


        # action.drag_and_drop_by_offset(slider_input, 0, 300)
        # action.perform()
        time.sleep(10)





take_picture = NoTest()
take_picture.login_site()

take_picture.take_picture()


take_picture.driver.close()
# //span[@class='number' and text()='49']
# div.viewFrontBack
