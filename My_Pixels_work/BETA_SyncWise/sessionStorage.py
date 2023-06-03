import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager



class NoTest1:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login_site(self):
        """login site and enter"""
        base_url = 'https://beta.syncwise360.com/login'
        self.driver.get(base_url)
        self.driver.maximize_window()
        time.sleep(2)

        print('Start test')

        login_standard_user = "igorperetssuperior"
        password_all = "1234"

        # LOGIN PAGE
        # INPUT LOGIN
        user_name = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="username"]')))
        user_name.send_keys(login_standard_user)
        print('Input Login')

        # INPUT PASSWORD
        password = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password.send_keys(password_all)
        print('Input Password')

        # CLICK LOGIN BUTTON
        button_login = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="submit"]')))
        button_login.click()
        print('Click Login Button')
        time.sleep(10)

        # Поместите сюда ваш дополнительный код для выполнения действий после успешного входа на сайт

        # Пример: получение значения из sessionStorage
        script = 'return sessionStorage.getItem("key");'
        value = self.driver.execute_script(script)
        print('Value from sessionStorage:', value)

        # Закрытие браузера
        self.driver.quit()



run = NoTest1()
run.login_site()


