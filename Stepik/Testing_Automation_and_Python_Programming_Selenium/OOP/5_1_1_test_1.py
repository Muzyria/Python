import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test1:
    def test_select_product(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        base_url = 'https://demoqa.com/dynamic-properties'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(2)
        driver.close()


test = Test1()
test.test_select_product()

