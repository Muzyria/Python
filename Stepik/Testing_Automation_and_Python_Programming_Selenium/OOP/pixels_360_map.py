import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class NoTest1:

    def driwing_map(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        base_url = 'https://accounts.syncwise360.com/#login'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(2)

        print('Start test')

        login_standard_user = " "
        password_all = "  "

        #  LOGON PAGE
        user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login-form-username"]')))
        user_name.send_keys(login_standard_user)
        print('Input Login')

        password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login-form-password"]')))
        password.send_keys(password_all)
        print('Input Password')

        button_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="login-form-submit"]')))
        button_login.click()
        print('Click Login Button')
        # time.sleep(2)


        #  ASSERT TRACKER
        button_asset_tracker = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="nav-yamaha"]')))
        button_asset_tracker.click()
        print('Click Asset Tracker Button')

        #  Geofence Button
        button_geofence = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="button7 bsize9 vertical-box-center btn-geofence"]')))
        button_geofence.click()
        print('Click Geofence Button')
        # time.sleep(5)


        #  ADD Geofence
        button_add_geofence = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="button4 rectangle btn-add"]')))
        button_add_geofence.click()
        print('Click ADD Geofence Button')
        # time.sleep(5)

        #  INPUT NAME Geofence
        input_name_geofence = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="name"]')))
        input_name_geofence.send_keys('My_Test_geofence')
        print('Input NAME GEOFENCE')
        time.sleep(2)


        #  Рисуем геофенс -------------------->

        actions = ActionChains(driver)
        map_geofence = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//canvas[@id="Microsoft.Maps.Imagery.Aerial"]')))


        # actions.move_by_offset(100, 10).perform()
        actions.move_by_offset(100, 100)
        actions.click().perform()
        time.sleep(1)

        actions.move_by_offset(100, 200)
        actions.click().perform()
        time.sleep(1)

        # actions.move_by_offset(200, 200)
        # actions.click().perform()
        # time.sleep(1)
        #
        # actions.move_by_offset(200, 100)
        # actions.click().perform()
        # time.sleep(1)

        # actions.click().perform()

        # actions.click(map_geofence).move_by_offset(1, 1).perform()
        # actions.click(map_geofence).move_by_offset(100, 1).perform()
        # actions.click(map_geofence).move_by_offset(100, 100).perform()
        # actions.click(map_geofence).move_by_offset(1, 100).perform()

        #action.click_and_hold(slider).move_by_offset(250, 0).release().perform()
        # actions.click().perform()
        time.sleep(4)



test = NoTest1()
test.driwing_map()

