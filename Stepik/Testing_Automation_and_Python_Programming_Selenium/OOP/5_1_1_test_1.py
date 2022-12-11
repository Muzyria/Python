import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class NoTest1:

    def select_product(self):
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        s = Service(r'C:\Git_Muzyria\Python\Stepik\Testing_Automation_and_Python_Programming_Selenium\OOP\resource'
                    r'\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        base_url = 'https://demoqa.com/dynamic-properties'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(5)


test = NoTest1()
test.select_product()

