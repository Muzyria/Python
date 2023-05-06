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

    def login_site(self):
        """login site and enter"""
        base_url = 'https://sandbox.syncwise360.com/login'
        self.driver.get(base_url)
        self.driver.maximize_window()
        time.sleep(2)

        print('Start test')

        login_standard_user = "igorperetssuperior"
        password_all = "1234"

        # LOGIN PAGE
        # INPUT LOGIN
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="username"]')))
        user_name.send_keys(login_standard_user)
        print('Input Login')

        # INPUT PASSWORD
        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password.send_keys(password_all)
        print('Input Password')

        # CLICK LOGIN BUTTON
        button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="submit"]')))
        button_login.click()
        print('Click Login Button')
        time.sleep(5)

    def assert_tracker_close_slide(self):
        """ASSERT TRACKER"""
        button_close_slidebar = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="closeSidebarbtn"]')))
        button_close_slidebar.click()
        print('Click Close SlideBar Button')
        time.sleep(3)

    def geofence_button_click(self):
        """Geofence Button click on right side screen"""
        button_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="geofenceZones"]')))
        button_geofence.click()
        print('Click Geofence Button')
        time.sleep(3)

    def choice_type_geofence(self):
        """click on drop-down list and select type of geofence"""
        drop_list_type_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="mat-select-trigger ng-tns-c67-0"]')))
        drop_list_type_geofence.click()
        print('click on drop-down list')
        time.sleep(1)

    def add_geofence_button_click(self):
        """ADD Geofence button click"""
        button_add_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="closeModal p-0 ng-star-inserted"]')))
        button_add_geofence.click()
        print('Click ADD Geofence Button')
        time.sleep(1)

    def input_name_geofence(self, id_number):
        """INPUT NAME Geofence"""
        input_name_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="ng-untouched ng-pristine ng-invalid"]')))
        input_name_geofence.send_keys(f'My_Test_geofence_{id_number}')
        print(f'Input NAME GEOFENCE {id_number}')
        time.sleep(1)

    def choice_command_geofence(self):
        # SELECT ListCommand Geofence
        select_command_list = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="ng-untouched ng-pristine ng-invalid"]')))
        select_command_list.click()
        print('Click select_command_list')
        time.sleep(2)
        # Select command
        select_command = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//option[text()="9 mph with beeping "]')))
        select_command.click()
        print('Click 9 mph with beeping ')
        # x = 1755
        # y = 653
        # pyautogui.moveTo(x, y)
        # pyautogui.click(button='left')
        # time.sleep(1)

    def input_custom_message(self):
        # Input Custom Message
        pyautogui.scroll(-300)
        time.sleep(1)
        select_message = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="helo"]/app-pages/div/div/div[2]/app-coursemap/div/div[1]/app-geofence/div[2]/div/div/form/ng-scrollbar/div/div/div/div/div/div[6]/textarea')))
        # select_message.click()
        select_message.send_keys("This geofence was created automatically")
        print('Click Clik Message')

    def canvas(self):
        """CANVAS"""
        obj_canvas = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'canvas[class="leaflet-zoom-animated"]')))
        location = obj_canvas.location
        size = obj_canvas.size
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']

        print("Границы элеиента: x={}, y={}, width={}, height={}".format(x, y, width, height))

        # Определяем центр и радиус круга
        random_coordinate_x = random.randint(-600, 200)
        random_coordinate_y = random.randint(-300, 300)
        center_x = random_coordinate_x  # X-координата центра круга (центр экрана = 0)
        center_y = random_coordinate_y  # Y-координата центра круга (центр экрана = 0)
        radius = 30  # Радиус круга

        # Определяем траекторию движения курсора
        num_points = 12  # Количество точек на траектории
        angle_increment = 2 * math.pi / num_points  # Шаг изменения угла
        speed = 0.01  # Скорость движения курсора

        # Создаем экземпляр ActionChains
        actions = ActionChains(self.driver)

        # Перемещаем курсор по траектории круга
        for i in range(num_points + 1):
            angle = i * angle_increment
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            actions.move_to_element_with_offset(obj_canvas, x, y).click().perform()
            time.sleep(speed)

    def canvas_2(self):
        """CANVAS 2 """
        obj_canvas = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'canvas[class="leaflet-zoom-animated"]')))
        self.driver.execute_script("""
            var ctx = arguments[0].getContext("2d");
            var centerX = 750;
            var centerY = 300;
            var radius = 100;
            var numPoints = 5;
            var angleIncrement = (2 * Math.PI) / numPoints;

            ctx.beginPath();
            for (var i = 0; i < numPoints * 2; i++) {
                var angle = i * angleIncrement;
                var x, y;
                if (i % 2 === 0) {
                    x = centerX + radius * Math.cos(angle);
                    y = centerY + radius * Math.sin(angle);
                } else {
                    x = centerX + radius / 2 * Math.cos(angle);
                    y = centerY + radius / 2 * Math.sin(angle);
                }
                if (i === 0) {
                    ctx.moveTo(x, y);
                } else {
                    ctx.lineTo(x, y);
                }
            }
            ctx.closePath();
            ctx.fillStyle = "yellow";
            ctx.fill();
        """, obj_canvas)

    def canvas_3(self):
        """CANVAS 3 """
        canvas = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'canvas[class="leaflet-zoom-animated"]')))
        # Создаем экземпляр ActionChains
        actions = ActionChains(self.driver)
        center_x = -600
        center_y = -100
        outer_radius = 40
        inner_radius = outer_radius / 4
        num_points = 4  # Количество вершин звезды
        angle_increment = 2 * math.pi / num_points

        for i in range(num_points + 1):
            outer_angle = i * angle_increment
            inner_angle = outer_angle + angle_increment / 2

            outer_x = center_x + outer_radius * math.cos(outer_angle)
            outer_y = center_y + outer_radius * math.sin(outer_angle)
            inner_x = center_x + inner_radius * math.cos(inner_angle)
            inner_y = center_y + inner_radius * math.sin(inner_angle)

            actions.move_to_element_with_offset(canvas, outer_x, outer_y).click().perform()
            actions.move_to_element_with_offset(canvas, inner_x, inner_y).click().perform()

            time.sleep(0.01)  # Пауза для наглядности

    def canvas_4(self):
        """CANVAS 4"""
        obj_canvas = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'canvas[class="leaflet-zoom-animated"]')))
        location = obj_canvas.location
        size = obj_canvas.size
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']

        print("Границы элемента: x={}, y={}, width={}, height={}".format(x, y, width, height))

        obj_pop_div_menu = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="commonPopup"]')))
        location_div_menu = obj_pop_div_menu.location
        size_div_menu = obj_pop_div_menu.size
        x_div = location_div_menu['x']
        y_div = location_div_menu['y']
        width_div = size_div_menu['width']
        height_div = size_div_menu['height']

        print("Границы элемента div_menu: x={}, y={}, width={}, height={}".format(x_div, y_div, width_div, height_div))

        # Определяем

        center_x = 0  # X-координата центра (центр экрана = 0)
        center_y = 0  # Y-координата центра (центр экрана = 0)
        coordinate_x_start = (width // 2 - 100) * -1
        coordinate_x_finish = width // 2 - width_div - 100
        coordinate_y_start = (height // 2 - 100) * -1
        coordinate_y_finish = height // 2 - 100

        # Создаем экземпляр ActionChains
        actions = ActionChains(self.driver)

        # Перемещаем курсор по траектории
        print(coordinate_x_start, coordinate_y_start, coordinate_x_finish, coordinate_y_finish)

        actions.move_to_element_with_offset(obj_canvas, coordinate_x_start, coordinate_y_start).click().perform()  # -x -y
        print(coordinate_x_start, coordinate_y_start)
        actions.move_to_element_with_offset(obj_canvas, coordinate_x_finish, coordinate_y_start).click().perform()  # +x -y
        print(coordinate_x_finish, coordinate_y_start)
        actions.move_to_element_with_offset(obj_canvas, coordinate_x_finish, coordinate_y_finish).click().perform()  # +x +y
        print(coordinate_x_finish, coordinate_y_finish)
        actions.move_to_element_with_offset(obj_canvas, coordinate_x_start, coordinate_y_finish).click().perform()  # -x +y
        print(coordinate_x_start, coordinate_y_finish)
        actions.move_to_element_with_offset(obj_canvas, coordinate_x_start, coordinate_y_start).click().perform()  # -x -y


    def button_save_click(self):
        # Press Button SAVE
        button_add_geofence = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn"]')))
        button_add_geofence.click()
        print('Click SAVE Button')
        time.sleep(7)

    # @staticmethod
    # def action_draw():
    #     x, y, radius_val = 350, 700, 100
    #     count = 1
    #     for _ in range(3):
    #         x = 350
    #         for _ in range(1, 8):
    #             test.add_geofence(x, y, radius_val, count)
    #             x += 100
    #             count += 1
    #         y += 100


test = NoTest1()
test.login_site()
test.assert_tracker_close_slide()
test.geofence_button_click()
# test.choice_type_geofence()

test.add_geofence_button_click()
test.input_name_geofence('100')

test.canvas_4()


time.sleep(60)
test.driver.close()


