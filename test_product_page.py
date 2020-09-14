from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.product_page import Page_Object


class TestToBasket(Page_Object):
    def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        basket = Page_Object(browser)
        basket.add_book_to_basket()
        basket.solve_quiz_and_get_code()
        basket.open_to_basket()
        bookToCompare = basket.find_book_name()
        priceToCompare = basket.find_book_price()
        assert bookToCompare
        assert priceToCompare


