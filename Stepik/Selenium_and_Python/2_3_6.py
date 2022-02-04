from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link) #open link
    time.sleep(3)

    button0 = browser.find_element_by_class_name("trollface.btn.btn-primary").click()
    time.sleep(1)


    # switch new window
    new_window = browser.window_handles[1]
    print(new_window)
    browser.switch_to_window(new_window) # open new window
    
    x = browser.find_element_by_id("input_value").text 
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
    