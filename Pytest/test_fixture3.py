import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print()
    print("\nstart browser for test..")
    print()
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    # этот код выполнится после завершения теста
    print()
    print("\nquit browser..")
    print()
    browser.quit()


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
