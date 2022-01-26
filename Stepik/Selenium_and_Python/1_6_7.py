from selenium import webdriver
import time
import string
import random

letters = string.ascii_lowercase

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        random_word = ''.join(random.choice(letters) for _ in range(8))
        element.send_keys(random_word)
        element.send_keys(len(elements))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
