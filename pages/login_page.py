import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        substring = LoginPageLocators.CSS_SUBSTRING_LOGIN
        # проверка, что в адресе страницы есть "login"
        if substring in self.browser.current_url:
            return True
        return "No 'login' in url on this page!"


    def should_be_login_form(self):
        # проверка наличия формы логина
        if self.is_element_present(*LoginPageLocators.CSS_LOGIN_FORM):
            return True
        return "Login not form on page!"


    def should_be_register_form(self):
        # проверка наличия формы регистрации на странице
        if self.is_element_present(*LoginPageLocators.CSS_REG_FORM):
            return True
        return "No register form on page!"

    def make_email_and_pass(self):
        # генерация почты и передача пароля
        return (str(time.time()) + "@email.com", "Password_123")

    def register_new_user(self, email, password):
        # регистрация нового пользователя
        self.email = email
        self.password = password
        # находим элементы на странице: поля ввода почты, пароля и кнопку регистрации
        email_input = self.browser.find_element(*LoginPageLocators.CSS_LOGIN_INPUT_REG)
        pass_input = self.browser.find_element(*LoginPageLocators.CSS_REG_INPUT_PASS1)
        pass_confirm = self.browser.find_element(*LoginPageLocators.CSS_REG_INPUT_PASS2)
        reg_button = self.browser.find_element(*LoginPageLocators.CSS_REG_BUTTON)
        # вводим почту, пароль
        email_input.send_keys(email)
        pass_input.send_keys(password)
        pass_confirm.send_keys(password)
        # нажимаем на кнопку "зарегистрировать"
        reg_button.click()

