import selenium
from selenium import webdriver                                      # взаимодействие с веб-браузером: установление соединения и управление им
from selenium.webdriver.support.ui import WebDriverWait             # позволяет добавлять время ожидания в наши операции (настраивать явно и неявное ожидание)
from selenium.webdriver.common.by import By                         # выбор веб-элементов 
from selenium.webdriver.support import expected_conditions as EC    # выбор веб-элементов
from selenium.webdriver.chrome.options import Options               # предоставляет дополнительные опции для нашего веб-драйвера
from selenium.webdriver import ActionChains                         # методы для имитации действий мыши, необходимых для перетаскивания
from selenium.webdriver.support.select import Select                # класс используется для работы с выпадающими меню с одним или несколькими вариантами выбора с помощью HTML-тега
import time                                                         # добавляет неявное ожидание (то есть всегда)
import math                                                         # использование математических функций
import os                                                           # использование модуля для работы с ОС (например, при загрузке файлов на стенд)
import unittest                                                     # фреймворк, облегающий работу
import pytest                                                       # импорт фреймворка

# Локатор кнопки "Войти" на главной странице
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

# Локаторы в форме авторизации на странице "Войти или зарегистрироваться"
class LoginPageLocators ():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

# Локаторы в форме регистрации на странице "Войти или зарегистрироваться"
class RegistrationBaseLocators ():
    EMAIL_LINK = (By.NAME, 'registration-email')
    PASSWORD_LINK = (By.NAME, 'registration-password1')
    REPEAT_PASSWORD_LINK = (By.NAME, 'registration-password2')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

# Локаторы добавления товара в корзину
class ProductPageLocators ():
    # Локатор добавления товара в корзину
    ADD_TO_BUTTON = (By.CSS_SELECTOR, "button.btn-primary.btn-lg")

    # Локатор названия книги
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')

    # Локатор цены книги
    BOOK_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')

    # Локатор о добавлении товара в корзину
    MESSAGE_OF_ADDING_BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner strong")

    # Локатор суммы корзины
    MESSAGE_OF_SUM_OF_BASKET = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")