from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(int(x)+int(y)))
    browser.find_element_by_tag_name("button").click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



'''
from selenium import webdriver
import time

# Метод get_attribute

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link) #open link

    x = int(browser.find_element_by_id("num1").text)
    y = int(browser.find_element_by_id("num2").text)
    total = x + y

    list_1 = browser.find_elements_by_css_selector("#dropdown option")
    for element in list_1:
        sel_number = element.get_attribute("value")
        if sel_number.isdigit() and int(sel_number) == total:
            element.click()
            break
    
    browser.find_element_by_class_name("btn-default").click()

    time.sleep(5)

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''
'''
from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)

try:
    x = browser.find_element_by_css_selector("#num1").text
    y = browser.find_element_by_css_selector("#num2").text
    summ = int(x) + int(y)

    elements = browser.find_elements_by_css_selector("#dropdown option")
    for element in elements:
        select_num = element.get_attribute("value")
        if select_num.isdigit() and int(select_num) == summ:
            element.click()
            break

    browser.find_element_by_css_selector("form button[type=submit]").click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
    browser.close()

finally:
    browser.quit()
'''    