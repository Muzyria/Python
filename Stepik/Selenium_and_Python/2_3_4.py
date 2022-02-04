from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link) #open link

    button0 = browser.find_element_by_class_name("btn.btn-primary").click()
    time.sleep(1)

    alert = browser.switch_to.alert
    time.sleep(1)
    alert.accept()

    # open new window
    
    x = browser.find_element_by_id("input_value").text # get atribute
    #print("x=", x)
    y = calc(x)
    #print("y=", y)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y) # write answer

    button1 = browser.find_element_by_class_name("btn.btn-primary").click()

    alert = browser.switch_to.alert
    print(alert.text)
    time.sleep(1)
    alert.accept()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    