import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

from request import login, get_report

"""
Slot {'oe_22la', 'oe_vpt', 'oe_vt'} 3
Ukrgaztech {'floutek_tm_vr_1', 'floutek_tm_board2', 'pk_v', 'corrector_pc_2'} 4
Radmirtech {'kvr_1_02', 'kplg_1_01', 'vega_1_01', 'radio_modul', 'kplg_2_01r', 'tkb', 'vega_1_01_nvch', 'kvr_1_01n', 'kplg_1_02r', 'vega_2_01n', 'tkb_1', 'kplg_1_02rv', 'kvr_1_01', 'vega_1_01vch', 'vega_2_01', 'vega_1_01n'} 16
Vymiruvalnitechnologii {'v25'} 1
rgk {'smart104'} 1
Grempis {'universal_01', 'universal_m', 'universal_02', 'universal_mt'} 4
Tandem {'tandem_tr', 'tandem_t'} 2
Ukrgaztech_Imod {'corrector_pc_2'} 1
"""


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

    def list_pages(self):
        button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#qwertyd > nz-spin > div > nz-pagination > ul > li.ant-pagination-options.ng-star-inserted > nz-select > nz-select-top-control > nz-select-item')))
        button.click()
        time.sleep(2)
        button100 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="100 / стр."]')))
        button100.click()
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

    def click_pre_view(self):
        # CLICK  BUTTON
        button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '//*[text()="Предварительный просмотр"]')))
        button_login.click()
        print('Click pre view Button')

    def input_manufacture(self, data):
        input_manuf = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#qwertyd > nz-spin > div > div > nz-table-inner-default > div > table > thead > tr > th:nth-child(2) > nz-table-filter > span > div > input')))
        input_manuf.send_keys(data)
        print('input manufacture')

    def input_type_device(self, data):
        input_type = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#qwertyd > nz-spin > div > div > nz-table-inner-default > div > table > thead > tr > th:nth-child(3) > nz-table-filter > span > div > input')))
        input_type.send_keys(data)
        print('input type device')


test = NoTest()
test.login_site()
# test.report_page()
#
# test.list_pages()
# # test.click_check_box_all()
#
# test.input_manufacture('RGK')
# test.input_type_device('smart104')
time.sleep(10)