from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.ru")
input_gooole = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
input_gooole.send_keys("Iphone")
input_gooole.send_keys(Keys.RETURN)

assert "Iphone - Поиск в Google" in driver.title

time.sleep(3)
driver.quit()
