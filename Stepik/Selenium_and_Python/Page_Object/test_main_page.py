from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage(object):

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
        page = MainPage(browser, link)  # инициализируем Page, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_should_see_login_page_forms(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    """
    1. Гость открывает главную страницу
    2. Переходит в корзину по кнопке в шапке сайта
    3. Ожидаем, что в корзине нет товаров
    4. Ожидаем, что есть текст о том что корзина пуста

    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()  # Гость открывает главную страницу
    page.go_to_basket_page()  # Переходит в корзину по кнопке в шапке сайта
    cart_page = CartPage(browser, browser.current_url)  # Объект страницы корзины
    cart_page.should_not_be_product_in_basket()  # Ожидаем, что в корзине нет товаров
    cart_page.should_be_message_about_empty_basket()  # Ожидаем, что есть текст о том что корзина пуста
