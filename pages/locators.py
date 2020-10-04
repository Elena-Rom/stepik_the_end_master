from selenium.webdriver.common.by import By


class MainPageLocators():
    CSS_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/"

class LoginPageLocators():
    CSS_LOGIN_INPUT = (By.CSS_SELECTOR,'input[name="login-username"]')
    CSS_LOGIN_INPUT_PASS = (By.CSS_SELECTOR, 'input[name="login-password"]')
    CSS_LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    LOGIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    CSS_SUBSTRING_LOGIN = "login"
    CSS_LOGIN_FORM = (By.ID, "login_form")
    CSS_LOGIN_INPUT_REG = (By.ID, "id_registration-email")
    CSS_REG_INPUT_PASS1 = (By.ID, "id_registration-password1")
    CSS_REG_INPUT_PASS2 = (By.ID, "id_registration-password2")
    CSS_REG_BUTTON = (By.NAME, "registration_submit")

    CSS_REG_FORM = (By.ID, "register_form")

class ProductPageLocators():
    CSS_OPEN_BASKET = 'div.basket-mini a.btn-default'
    CSS_ADD_TO_BASKET = 'button.btn-add-to-basket'
    PRODUCT_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    PRODUCT_PAGE_PROMO = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    CSS_BOOK_TO_COMPARE = (By.CSS_SELECTOR, ".product_main h1")
    CSS_PRICE_TO_COMPARE = (By.CLASS_NAME, "price_color")
    CSS_ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    CSS_BOOK_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    CSS_PRICE_NUMBER = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    CSS_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")

class BasePageLocators():
    CSS_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CSS_LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CSS_BASKET_BUTTON_EN_GB = (By.LINK_TEXT, "View basket")
    CSS_BASKET_BUTTON_RU = (By.LINK_TEXT, "Посмотреть корзину")
    CSS_USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    CSS_BASKET_EMPTY = (By.ID, "content_inner")
    CSS_BASKET_NOT_EMPTY = (By.CLASS_NAME, "basket-title")
# "Ваша корзина пуста"
    SUBSTRING_BASKET_EN_GB = "Your basket is empty"
    SUBSTRING_BASKET_RU = "Ваша корзина пуста"


