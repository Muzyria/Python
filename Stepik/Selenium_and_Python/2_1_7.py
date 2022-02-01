from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link) #open link

    x = browser.find_element_by_id("treasure").get_attribute("valuex") # get atribute
    #print("x=", x)
    y = calc(x)
    #print("y=", y) 

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y) # write answer 

    check1 = browser.find_element_by_id("robotCheckbox")
    check1.click() # clik check_box

    radio1 = browser.find_element_by_id("robotsRule")
    radio1.click()

    button1 = browser.find_element_by_class_name("btn-default")
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    