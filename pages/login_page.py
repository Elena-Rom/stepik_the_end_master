from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.cant_url(LoginPageLocators.LOGIN_LINK)
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(LoginPageLocators.CSS_LOGIN_INPUT), "Login not an window"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(LoginPageLocators.CSS_LOGIN_INPUT_REGISTR), "Login register not an window"
        assert True