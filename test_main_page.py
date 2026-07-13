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

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.locators import BasePageLocators

def test_guest_can_go_to_login_page(browser):

    link = "http://selenium1py.pythonanywhere.com/"

    # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = MainPage(browser, link)

    # Открываем страницу 
    page.open()

    # Выполняем метод страницы — переходим на страницу логина                     
    page.go_to_login_page()

    # Пересоздаем переменную для нового теста
    login_page = LoginPage(browser, browser.current_url)

    # Выполняем тесты
    login_page.should_be_login_page()

product_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

@pytest.mark.xfail (reason = 'Тест упадет')
def test_guest_cant_see_success_message_after_adding_product_to_basket (browser):  

    page = ProductPage(browser, product_link)
    page.open ()
    page.test_guest_can_add_product_to_basket ()
    page.should_not_be_success_message ()

def test_guest_cant_see_success_message (browser):

    page = ProductPage(browser, product_link)
    page.open ()
    page.should_not_be_success_message ()
    
@pytest.mark.xfail (reason = 'Тест упадет')
def test_message_disappeared_after_adding_product_to_basket (browser):

    page = ProductPage(browser, product_link)
    page.open ()
    page.test_guest_can_add_product_to_basket ()
    page.should_disappear_success_message()

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/" 

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):

        page = ProductPage (browser, link)
        page.open ()
        page.go_to_login_page ()

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage (browser, link)
        page.open ()
        page.should_be_login_link ()