from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        self.shouldnt_be_any_product_in_basket()
        self.should_be_empty_basket_text()

    def shouldnt_be_any_product_in_basket(self):
        substring = BasketPageLocators.SUBSTRING_BASKET_EN_GB
        # проверка, что на странице присутствует строчка о пустой корзине
        if substring in self.browser.find_element(
            BasketPageLocators.CSS_BASKET_EMPTY).text:
            return True

    def should_be_empty_basket_text(self):
        # проверка, что на странице не появляется товаров, добавленных в корзину
        assert self.is_not_element_present(*BasketPageLocators.CSS_BASKET_NOT_EMPTY), "Basket is not empty, but it should!"

    def should_be_not_basket_text(self):
        # проверка, что на странице появляется товар, добавленный в корзину
        assert self.is_element_present(*BasketPageLocators.CSS_BASKET_NOT_EMPTY), "Basket is empty, but it shouldn't!"
