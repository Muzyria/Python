from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link) #open link

    x = browser.find_element_by_id("input_value").text # get atribute
    #print("x=", x)
    y = calc(x)
    #print("y=", y) 

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y) # write answer 

    check1 = browser.find_element_by_id("robotCheckbox")
    check1.click() # clik check_box

    
    
    radio1 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio1)
    radio1.click()

    button1 = browser.find_element_by_class_name("btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()