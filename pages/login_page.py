from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegistrationBaseLocators

from faker import Faker
fake = Faker ()

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

    def register_new_user(self):
        email_link = self.browser.find_element (*RegistrationBaseLocators.EMAIL_LINK)
        email_link.click ()
        email_link.send_keys (fake.email ())
        print ('Поле электронной почты заполнено')

        password_link = self.browser.find_element (*RegistrationBaseLocators.PASSWORD_LINK)
        password_link.click ()
        password_link.send_keys ('Cfifcfifcfif')
        print ('Поле пароля заполнено')

        repeat_password_link = self.browser.find_element (*RegistrationBaseLocators.REPEAT_PASSWORD_LINK)
        repeat_password_link.click ()
        repeat_password_link.send_keys ('Cfifcfifcfif')
        print ('Поле повторения пароля заполнено')

        press_button_of_registration = self.browser.find_element (*RegistrationBaseLocators.BUTTON_REGISTRATION)
        press_button_of_registration.click ()
        print ('Кнопка Зарегистрировать нажата')