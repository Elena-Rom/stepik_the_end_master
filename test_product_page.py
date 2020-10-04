import pytest

from pages.locators import LoginPageLocators, ProductPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import PageProduct
import _pytest

'''#данные для теста с параметризацией, сейчас не используются
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])'''
class TestToBasket(PageProduct):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, timeout=5):
        link = LoginPageLocators.LOGIN_PAGE_LINK  # ссылка на страницу логина\регистрации
        self.browser = browser
        # неявное ожидание
        self.browser.implicitly_wait(timeout)
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = LoginPage(browser, link)
        page.open()
        # генерим тестовую почту, задаем пароль
        email_password = page.make_email_and_pass()
        # регистрируем нового пользователя
        page.register_new_user(*email_password)
        # проверяем, что пользователь авторизован
        #page.should_be_authorized_user()  # на деле такие проверки лучше не делать (setup не для этого)

    def test_guest_can_add_product_to_basket(self,browser):
            link = ProductPageLocators.PRODUCT_PAGE_PROMO
            # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
            page = PageProduct(browser, link)
            page.open()
            bookToCompare = page.find_book_name()
            priceToCompare = page.find_book_price()
            # добавляем товар в корзину
            page.add_item_to_cart()
            page.solve_quiz_and_get_code()
            # проверяем, что название и цена книги верные
            assert  page.right_book_and_right_price_message(bookToCompare, priceToCompare)

    def test_user_cant_see_success_message(self, browser):
            link = ProductPageLocators.PRODUCT_PAGE_LINK
            # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
            page = PageProduct(browser, link)
            page.open()
            assert page.should_not_be_success_message(), "Success message is presented, but should not be"


    def test_guest_should_see_login_link_on_product_page(browser):
        # проверка, что пользователь "видит" кнопку логина на странице продукта
        link = ProductPageLocators.PRODUCT_PAGE_LINK
        page = PageProduct(browser, link)
        page.open()
        assert (page.should_be_login_link())

    def test_guest_can_go_to_login_page_from_product_page(browser):
        # проверка, что пользователь может перейти на страницу логина со страницы продукта
        link = ProductPageLocators.PRODUCT_PAGE_LINK
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        page.open()
        # выполняем метод страницы: переходим на страницу логина
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        # проверка, что перешли действительно на страницу логина
        assert (login_page.should_be_login_page())

    def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
        link = ProductPageLocators.PRODUCT_PAGE_LINK
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        # открываем нужную страницу
        page.open()
        page.go_to_basket_page()
        cart_page = PageProduct(browser, browser.current_url)
        # проверка, что в корзине нет товаров и есть сообщение о пустой корзине
        cart_page.cart_should_be_empty()











