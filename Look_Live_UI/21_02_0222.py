from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
try:

    driver.get("https://unsplash.com")

    time.sleep(1)

    btn_input = driver.find_element(By.XPATH, '//*[@id="popover-visual-search-form-homepage-header"]/button').click()

    time.sleep(1)

    input_img = driver.find_element(By.XPATH, '//*[@id="popover-visual-search-form-homepage-header"]/div/div/div/div/div/div[2]/div/div[1]/div/input').send_keys('C:\AQA_Python\\file.jpg')
    

finally:
    time.sleep(5)

    driver.quit()
