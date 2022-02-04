from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    input2.send_keys("Ivanov")

    input3 = browser.find_element_by_css_selector('[placeholder="Enter email"]')
    input3.send_keys("Ivan@sobaka.ru")



    #with open("test.txt", "w") as file:
        #content = file.write("automationbypython")  # create test.txt file
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    browser.find_element_by_css_selector('[type="file"]').send_keys(file_path)



    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    