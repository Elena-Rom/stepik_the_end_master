from pages.main_page import MainPage
from .locators import LocatorsPageProduct

class Page_Object(MainPage):
    def open_to_basket(self):
        basket = self.browser.find_element(LocatorsPageProduct.CSS_OPEN_BASKET)
        basket.click()

    def add_book_to_basket(self):
        self.click(LocatorsPageProduct.CSS_ADD_TO_BASKET)