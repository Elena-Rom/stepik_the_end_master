from pages.main_page import MainPage
from pages.locators import ProductPageLocators, BasketPageLocators

class PageProduct(MainPage):
    def open_to_basket(self):
        self.browser.find_element(ProductPageLocators.CSS_OPEN_BASKET).click()

    #def add_book_to_basket(self):
        #self.click(ProductPageLocators.CSS_ADD_TO_BASKET)

    def should_be_right_book_name(self, bookToCompare):
        # проверка сообщения о добавлении в корзину нужной книги
        if (self.browser.find_element(ProductPageLocators.CSS_BOOK_NAME).text == bookToCompare): #"No added book in a cart!"
            return True

    def should_be_right_price_for_book(self, priceToCompare):
        # проверка сообщения о цене товара в корзине
        if (self.browser.find_element(ProductPageLocators.CSS_PRICE_NUMBER).text == priceToCompare): #"Wrong price for the book!"
            return True

    def find_book_name(self):
        return self.browser.find_element(ProductPageLocators.CSS_BOOK_TO_COMPARE).text

    def find_book_price(self):
        return self.browser.find_element(ProductPageLocators.CSS_PRICE_TO_COMPARE).text

    def add_item_to_cart(self):
        # находим кнопку и добавляем товар в корзину
        self.browser.find_element(*ProductPageLocators.CSS_ADD_TO_CART_BUTTON).click()

    def right_book_and_right_price_message(self, bookToCompare, priceToCompare):
        self.should_be_right_book_name(bookToCompare)
        self.should_be_right_price_for_book(priceToCompare)

    def should_not_be_success_message(self):
        # проверка, что элемент не появился, так как не должен был
        if self.is_not_element_present(
            *ProductPageLocators.CSS_SUCCESS_MESSAGE):
            return True

    def should_disappear(self):
        # проверка, что элемент исчез
        assert self.is_disappeared(*ProductPageLocators.CSS_SUCCESS_MESSAGE), "Message is not disappeared, but should"


