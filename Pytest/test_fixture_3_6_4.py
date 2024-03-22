import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from webdriver_manager.opera import OperaDriverManager
import math
@pytest.fixture(scope="function")
def browser():
    print("___USE SECOND FIXTURE__")
    print("\nstart browser for test..")
    # browser = webdriver.Opera(service=Service(OperaDriverManager().install()))

    webdriver_service = service.Service(OperaDriverManager().install())
    webdriver_service.start()

    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', True)

    browser = webdriver.Remote(webdriver_service.service_url, options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()

def code():
    answer = math.log(int(time.time()))
    return answer

def test_guest_should_see_login_link(browser):
    link = f"https://stepik.org/lesson/236895/step/1"

    # Открытие браузера и переход на пустую страницу
    browser.get("about:blank")
    time.sleep(15)

    browser.get(link)
    time.sleep(5)


    # button = browser.find_element(By.ID, "ember416")
    button = browser.find_element(By.CSS_SELECTOR, "#ember416")
    button.click()
    time.sleep(1)

    email_field = browser.find_element(By.ID, "id_login_email")
    email_field.send_keys("Fila090580@gmail.com")
    time.sleep(1)

    password_field = browser.find_element(By.ID, "id_login_password")
    password_field.send_keys("5250")
    time.sleep(1)

    # button_submit = browser.find_element(By.CLASS_NAME, "sign-form__btn button_with-loader")
    button_submit = browser.find_element(By.CSS_SELECTOR, "#login_form > button")
    button_submit.click()
    time.sleep(10)

    print(code())
    time.sleep(30)

    password_field1 = browser.find_element(By.CSS_SELECTOR, '#ember492')
    password_field1.send_keys(str(code()))

    # time.sleep(1)

    button_submit1 = browser.find_element(By.CLASS_NAME, "submit-submission")
    button_submit1.click()


    time.sleep(40)
