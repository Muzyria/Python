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
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def driwing_map(self):

        base_url = 'https://accounts.syncwise360.com/#login'
        self.driver.get(base_url)
        self.driver.maximize_window()
        time.sleep(2)

        print('Start test')

        login_standard_user = "nessayurassic"
        password_all = "10583021"

        #  LOGON PAGE
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login-form-username"]')))
        user_name.send_keys(login_standard_user)
        print('Input Login')

        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login-form-password"]')))
        password.send_keys(password_all)
        print('Input Password')

        button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="login-form-submit"]')))
        button_login.click()
        print('Click Login Button')
        # time.sleep(2)

        #  ASSERT TRACKER
        button_asset_tracker = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="nav-yamaha"]')))
        button_asset_tracker.click()
        print('Click Asset Tracker Button')

        #  Geofence Button
        button_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="button7 bsize9 vertical-box-center btn-geofence"]')))
        button_geofence.click()
        print('Click Geofence Button')
        # time.sleep(5)


    def add_geofence(self, center_x, center_y, radius, ind):
        #  ADD Geofence
        button_add_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="button4 rectangle btn-add"]')))
        button_add_geofence.click()
        print('Click ADD Geofence Button')
        time.sleep(1)

        #  INPUT NAME Geofence
        input_name_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="name"]')))
        input_name_geofence.send_keys(f'1_DELETE_My_Test_geofence_{ind}')
        print(f'Input NAME GEOFENCE {ind}')
        # time.sleep(1)

        select_command_list = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="id_geofenceActionType"]')))
        select_command_list.click()
        print('Click select_command_list')
        # time.sleep(1)

        select_immediate_command = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//option[text()="Immediate shutdown"]')))
        select_immediate_command.click()
        print('Click Immediate shutdown')
        # time.sleep(1)


        #  Рисуем геофенс -------------------------------------------------------------------------->
        # Устанавливаем центр окружности
        center_x, center_y = center_x, center_y
        # Устанавливаем радиус окружности
        radius = radius
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

        pyautogui.press('enter')

        button_add_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="button save stretched-box"]')))
        button_add_geofence.click()
        print('Click SAVE Button')

        time.sleep(2)



test = NoTest1()
test.driwing_map()

x, y, radius_val = 100, 400, 50
for i in range(1, 10):
    test.add_geofence(x, y, radius_val, i)
    x += 100
# test.add_geofence(200, 400, 50, 1)
test.driver.close()


