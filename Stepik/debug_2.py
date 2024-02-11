

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension(fr'C:\Users\FILA\Desktop\coordinates.crx')

#with webdriver.Chrome(ChromeDriverManager().install()) as driver: # webdriver.Chrome(service=Service(ChromeDriverManager().install()))
with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options_chrome) as driver:

    driver.get('https://google.com')
    time.sleep(30)
