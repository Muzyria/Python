# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element(By.ID, "submit")

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service(r'/usr/local/bin/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!
driver.quit()
