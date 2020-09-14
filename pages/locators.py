from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    CSS_LOGIN_INPUT = (By.CSS_SELECTOR,'input[name="login-username"]')
    CSS_LOGIN_INPUT_PASS = (By.CSS_SELECTOR, 'input[name="login-password"]')
    CSS_LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    CSS_LOGIN_INPUT_REGISTR = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    CSS_REGISTR_INPUT_PASS1 = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    CSS_REGISTR_INPUT_PASS2 = (By.CSS_SELECTOR,'input[name="registration-password2"]')
    CSS_REGISTR_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class LocatorsPageProduct:
     CSS_OPEN_BASKET = 'div.basket-mini a.btn-default'
     CSS_ADD_TO_BASKET = 'button.btn-add-to-basket'

class LocatorsProductPage():
    PRODUCT_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    PRODUCT_PAGE_PROMO = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    BOOK_TO_COMPARE = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_TO_COMPARE = (By.CLASS_NAME, "price_color")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRICE_NUMBER = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")
