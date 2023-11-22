import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class NoTest:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login_site(self):
        """login site and enter"""
        base_url = 'https://direct-dev.hasgas.com.ua/login'
        self.driver.get(base_url)
        self.driver.maximize_window()
        time.sleep(2)

        print('Start test')

        login_standard_user = "MainAdminDirect"
        password_all = "6AQyk4nDaI4"

        # CLICK DROP-down LIST LANGUAGE
        language_list = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.dropbtn')))
        language_list.click()
        print('Click Language List')
        # time.sleep(1)

        # SELECT LANGUAGE
        language_ru = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="RU"]')))
        language_ru.click()
        print('Select Language RU')

        # LOGIN PAGE
        # INPUT LOGIN
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-login/div/div/div/app-login-block/div/form/div[1]/input')))
        user_name.send_keys(login_standard_user)
        print('Input Login')

        # INPUT PASSWORD
        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-login/div/div/div/app-login-block/div/form/div[2]/input')))
        password.send_keys(password_all)
        print('Input Password')

        # CLICK LOGIN BUTTON
        button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.btn-login')))
        button_login.click()
        print('Click Login Button')
        time.sleep(5)

    def report_page(self):
        # CLICK REPORT BUTTON
        button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Отчеты"]')))
        button_login.click()
        print('Click Report Button')
        time.sleep(5)

    def click_button_generate(self):
        # CLICK REPORT BUTTON
        button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section.section - button div.button - generate')))
        button_login.click()
        print('Click Generate Button')

    def click_check_box_all(self):
        check_box_kgs = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.check-box.check-box-ksg input')))
        check_box_kgs.click()
        print('Click KGS CheckBox')
        check_box_kkorr = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.check-box.check-box-kkorr input')))
        check_box_kkorr.click()
        print('Click KKORR CheckBox')


test = NoTest()
test.login_site()
test.report_page()
test.click_check_box_all()
time.sleep(5)