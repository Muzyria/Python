from selenium import webdriver

import pytest

import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize(
    'link', 
    [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ]
    )
def test_parametrise(browser, link):
    browser.get(link)

    answer = str(math.log(int(time.time())))

    input_text = browser.find_element_by_css_selector(".attempt textarea")
    input_text.send_keys(answer)

    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    text_field = browser.find_element_by_css_selector(".smart-hints__hint")
    text = text_field.text
    assert text == "Correct!", \
        f"expected 'Correct!', got {text}"  