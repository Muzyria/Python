

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


with webdriver.Chrome(ChromeDriverManager().install()) as driver:
    driver.get("https://google.com")
    time.sleep(5)