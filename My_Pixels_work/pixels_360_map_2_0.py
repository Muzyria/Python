import math
import random
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

        base_url = 'https://sandbox.syncwise360.com/login'
        self.driver.get(base_url)
        self.driver.maximize_window()
        time.sleep(2)

        print('Start test')

        login_standard_user = "igorperetssuperior"
        password_all = "1234"

        #  LOGIN PAGE
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="username"]')))
        user_name.send_keys(login_standard_user)
        print('Input Login')

        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password.send_keys(password_all)
        print('Input Password')

        button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="helo"]/app-auth/app-login/form/div/div/div[2]/div/div[2]/div[3]/button')))
        button_login.click()
        print('Click Login Button')
        time.sleep(20)

        #  ASSERT TRACKER
        button_close_slidebar = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="closeSidebarbtn"]')))
        button_close_slidebar.click()
        print('Click Close SlideBar Button')
        time.sleep(3)

        #  Geofence Button
        button_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="geofenceZones"]')))
        button_geofence.click()
        print('Click Geofence Button')
        time.sleep(3)

    def add_geofence(self, center_x, center_y, radius, ind):
        #  ADD Geofence
        button_add_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="closeModal p-0 ng-star-inserted"]')))
        button_add_geofence.click()
        print('Click ADD Geofence Button')
        time.sleep(1)

        #  INPUT NAME Geofence
        input_name_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="ng-untouched ng-pristine ng-invalid"]')))
        input_name_geofence.send_keys(f'Please_DELETE_My_Test_geofence_{ind}')
        print(f'Input NAME GEOFENCE {ind}')
        time.sleep(1)

        # SELECT ListCommand Geofence
        select_command_list = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="ng-untouched ng-pristine ng-invalid"]')))
        select_command_list.click()
        print('Click select_command_list')
        time.sleep(2)
        # Select command
        select_command = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//option[text()="9 mph with beeping "]')))
        select_command.click()
        print('Click 9 mph with beeping ')
        x = 1485
        y = 693
        pyautogui.moveTo(x, y)
        pyautogui.click(button='left')
        time.sleep(1)



        # Input Custom Message
        pyautogui.scroll(-300)
        time.sleep(1)

        select_message = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="helo"]/app-pages/div/div/div[2]/app-coursemap/div/div[1]/app-geofence/div[2]/div/div/form/ng-scrollbar/div/div/div/div/div/div[6]/textarea')))
        # select_message.click()
        select_message.send_keys("This geofence was created automatically")

        print('Click Clik Message')


        #  Рисуем геофенс -------------------------------------------------------------------------->
        # Устанавливаем центр окружности
        center_x, center_y = center_x, center_y
        # Устанавливаем радиус окружности
        radius = radius
        # Вычисляем количество шагов для обхода окружности
        num_steps = int(420 / 60)
        # Вычисляем шаг угла для каждого шага
        step_angle = 60 * math.pi / 180
        # Устанавливаем задержку между шагами
        pyautogui.PAUSE = 0.1
        # Движение курсора по окружности
        for i in range(num_steps):
            # Вычисляем координаты точки на окружности
            x = center_x + radius * math.cos(i * step_angle)
            y = center_y + radius * math.sin(i * step_angle)
            # Перемещаем курсор на новые координаты
            pyautogui.moveTo(x, y)
            pyautogui.click(button='left')

        # pyautogui.click(button='left')

        # Press Button SAVE
        button_add_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn"]')))
        button_add_geofence.click()
        print('Click SAVE Button')
        time.sleep(7)

    @staticmethod
    def action_draw():
        x, y, radius_val = 350, 700, 50
        count = 1
        for _ in range(3):
            x = 350
            for _ in range(1, 8):
                test.add_geofence(x, y, radius_val, count)
                x += 100
                count += 1
            y += 100


    def add_randome_geofence(self):
        #  ADD Geofence
        button_add_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="closeModal p-0 ng-star-inserted"]')))
        button_add_geofence.click()
        print('Click ADD Geofence Button')
        time.sleep(1)

        #  INPUT NAME Geofence
        input_name_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="ng-untouched ng-pristine ng-invalid"]')))
        input_name_geofence.send_keys(f'Please_DELETE_My_Test_geofence_R')
        print(f'Input NAME GEOFENCE R')
        time.sleep(1)

        # SELECT ListCommand Geofence
        select_command_list = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="ng-untouched ng-pristine ng-invalid"]')))
        select_command_list.click()
        print('Click select_command_list')
        time.sleep(2)
        # Select command
        select_command = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//option[text()="9 mph with beeping "]')))
        select_command.click()
        print('Click 9 mph with beeping ')
        x = 1485
        y = 693
        pyautogui.moveTo(x, y)
        pyautogui.click(button='left')
        time.sleep(1)



        # Input Custom Message
        pyautogui.scroll(-300)
        time.sleep(1)

        select_message = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="helo"]/app-pages/div/div/div[2]/app-coursemap/div/div[1]/app-geofence/div[2]/div/div/form/ng-scrollbar/div/div/div/div/div/div[6]/textarea')))
        # select_message.click()
        select_message.send_keys("This geofence was created automatically")

        print('Click Clik Message')


        #  Рисуем геофенс -------------------------------------------------------------------------->
        start_x, start_y = 300, 450
        pyautogui.moveTo(start_x, start_y)
        pyautogui.click(button='left')
        pyautogui.PAUSE = 0.15

        for i in range(500):
            pyautogui.moveTo(random.randrange(300, 900), random.randrange(450, 850))
            pyautogui.click(button='left')
            # Устанавливаем задержку между шагами
            pyautogui.PAUSE = 0.15

        pyautogui.moveTo(start_x, start_y)
        pyautogui.click(button='left')
        pyautogui.PAUSE = 0.15

        # Press Button SAVE
        button_add_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn"]')))
        button_add_geofence.click()
        print('Click SAVE Button')
        time.sleep(7)

test = NoTest1()
test.driwing_map()

# test.action_draw()
# test.add_geofence(300, 450, 50, 1)
test.add_randome_geofence()

test.driver.close()


