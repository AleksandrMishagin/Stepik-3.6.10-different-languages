from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверяем, что в текущем URL присутствует слово "login"
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, (f"Ожидался URL, содержащий 'login', но текущий URL: '{self.browser.current_url}'")

    # Проверяем, что элемент формы логина присутствует на странице
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма авторизации (Login form) не найдена на странице"

    # Проверяем, что элемент формы регистрации присутствует на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации (Register form) не найдена на странице"