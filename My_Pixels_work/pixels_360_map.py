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


class NoTest1:

    def driwing_map(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        base_url = 'https://accounts.syncwise360.com/#login'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(2)

        print('Start test')

        login_standard_user = "nessayurassic"
        password_all = "10583021"

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

        # actions = ActionChains(driver)
        # time.sleep(5)
        #
        # actions.move_by_offset(200, 200).click().perform()
        # actions.move_by_offset(70, 0).click().perform()
        # actions.move_by_offset(0, 70).click().perform()
        # actions.move_by_offset(-70, 0).click().perform()

        # Устанавливаем центр окружности
        center_x, center_y = 500, 500
        # Устанавливаем радиус окружности
        radius = 150
        # Вычисляем количество шагов для обхода окружности
        num_steps = int(360 / 60)
        # Вычисляем шаг угла для каждого шага
        step_angle = 60 * math.pi / 180
        # Устанавливаем задержку между шагами
        pyautogui.PAUSE = 0.01
        # Движение курсора по окружности
        for i in range(num_steps):
            # Вычисляем координаты точки на окружности
            x = center_x + radius * math.cos(i * step_angle)
            y = center_y + radius * math.sin(i * step_angle)
            # Перемещаем курсор на новые координаты
            pyautogui.moveTo(x, y)
            pyautogui.click(button='left')



        time.sleep(5)
        time.sleep(4)


test = NoTest1()
test.driwing_map()

