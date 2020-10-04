from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_should_see_login_link(self, browser):
        link = MainPageLocators.MAIN_PAGE_LINK
        #передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        page.open()
        # выполняем метод страницы: ищем переход на страницу логина
        assert (page.should_be_login_link()), "Login link is not presented"

    def test_guest_can_go_to_login_page(self, browser):
        link = MainPageLocators.MAIN_PAGE_LINK
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)  # выполняем метод страницы - переходим на страницу логина
        assert (login_page.should_be_login_page()), "No go page to login"


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = MainPageLocators.MAIN_PAGE_LINK
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    # открываем нужную страницу
    page.open()
    page.go_to_basket_page()
    cart_page = BasketPage(browser, browser.current_url)
    # проверка, что корзина пустая
    assert (cart_page.shouldnt_be_any_product_in_basket()), "No message of empty basket!"
