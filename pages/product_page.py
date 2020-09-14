from pages.main_page import MainPage
from .locators import LocatorsPageProduct, LocatorsProductPage

class Page_Object(MainPage):
    def open_to_basket(self):
        basket = self.browser.find_element(LocatorsPageProduct.CSS_OPEN_BASKET)
        basket.click()


    def add_book_to_basket(self):
        self.click(LocatorsPageProduct.CSS_ADD_TO_BASKET)

    def should_be_right_book_name(self, bookToCompare):
        # проверка сообщения о добавлении в корзину нужной книги
        assert self.browser.find_element(*LocatorsProductPage.BOOK_NAME).text == bookToCompare, "No added book in a cart!"

    def should_be_right_price_for_book(self, priceToCompare):
        # проверка сообщения о цене товара в корзине
        assert self.browser.find_element(*LocatorsProductPage.PRICE_NUMBER).text == priceToCompare, "Wrong price for the book!"

    def find_book_name(self):
        return self.browser.find_element(*LocatorsProductPage.BOOK_TO_COMPARE).text

    def find_book_price(self):
        return self.browser.find_element(*LocatorsProductPage.PRICE_TO_COMPARE).text