from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
try:

    driver.get("https://grinfer.com")

    btn_log_in = driver.find_element(By.XPATH, '//*[@id="page-root"]/div[1]/div[2]/div[2]/ul/a[1]').click()

    time.sleep(1)

    input_email = driver.find_element(By.ID, "email").send_keys("xxx@xxx.ru")
    input_email = driver.find_element(By.ID, "password").send_keys("12346789")

    btn_submit = driver.find_element(By.XPATH, '//*[@id="page-root"]/div[2]/div/div[2]/form/div/div[3]/button').click()



finally:
    time.sleep(5)

    driver.quit()
