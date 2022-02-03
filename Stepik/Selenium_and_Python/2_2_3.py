from selenium import webdriver
import time

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

    time.sleep(3)

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
    time.sleep(5)
    browser.close()

finally:
    browser.quit()
