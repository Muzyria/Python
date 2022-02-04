from selenium import webdriver
import time

browser = webdriver.Chrome()

time.sleep(2)
#browser.execute_script("alert('Robots at work');")
browser.execute_script("document.title='Страничка для Сережи';alert('Сережа начинай работать !');")
time.sleep(10)

browser.quit()