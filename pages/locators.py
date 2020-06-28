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
