import math
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


class RoutePreview:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def drive_map(self):

        base_url = 'https://www.google.com/intl/ru/maps/about/mymaps/'
        self.driver.get(base_url)
        self.driver.maximize_window()
        time.sleep(5)

        print('Start -----')

        # login_standard_user = "nessayurassic"
        # password_all = "10583021"
        #
        # #  LOGON PAGE
        # user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login-form-username"]')))
        # user_name.send_keys(login_standard_user)
        # print('Input Login')
        #
        # password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login-form-password"]')))
        # password.send_keys(password_all)
        # print('Input Password')
        #
        button_mymaps = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'p a[class="mymaps-cta"]')))
        button_mymaps.click()
        print('Click Button MyMaps')
        time.sleep(2)
        #
        # #  ASSERT TRACKER
        # button_asset_tracker = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="nav-yamaha"]')))
        # button_asset_tracker.click()
        # print('Click Asset Tracker Button')
        #
        # #  Geofence Button
        # button_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="button7 bsize9 vertical-box-center btn-geofence"]')))
        # button_geofence.click()
        # print('Click Geofence Button')
        # # time.sleep(5)






route = RoutePreview()

route.drive_map()



route.driver.close()


