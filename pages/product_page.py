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
 
from selenium.common.exceptions import NoAlertPresentException # в начале файла

from .base_page import BasePage
from .locators import ProductPageLocators
from .main_page import MainPage

class ProductPage (BasePage):

    # Находим имя книги
    def name_of_book (self):
        book_name = self.browser.find_element (*ProductPageLocators.BOOK_NAME)
        print (f'Название книги', book_name.text)
        return book_name.text

    # Находим цену книги
    def price_of_book (self):
        book_price = self.browser.find_element (*ProductPageLocators.BOOK_PRICE)
        print (f'Стоимость книги', book_price.text)
        return book_price.text
    
    # Находим кнопку "Войти" и кликаем её
    def test_guest_can_add_product_to_basket (self):
        button_link1 = self.browser.find_element (*ProductPageLocators.ADD_TO_BUTTON)
        button_link1.click ()
        
    # Переводим фокус на окно с оповещением, решаем уравнение, вводим решение в поле, принимаем предупреждение
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented") 

    # Находим имя книги в сообщении о добавлении книги в корзину, сравниваем его с изначальным названием книги
    def assert_book_name (self, Book7):
        Book_message =  WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(ProductPageLocators.MESSAGE_OF_ADDING_BOOK_IN_BASKET))
        assert Book7 == Book_message.text, 'Ошибка сравнения имени книги'
        print ("Имя текста книги сходится")
    
    # Находим сумму товаров в корзине, сравниваем его с ценой книги, добавленной в корзину
    def assert_book_price (self, Book8):
        Book_price2 = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(ProductPageLocators.MESSAGE_OF_SUM_OF_BASKET))
        assert Book8 == Book_price2.text, 'Ошибка сравнения цены книги'
        print ('Цена книги и суммы корзины сходится')

    def should_not_be_success_message(self):
        assert self.is_not_element_present (*ProductPageLocators.MESSAGE_OF_ADDING_BOOK_IN_BASKET), 'Сообщение отображается, но не должно быть'

    def should_disappear_success_message(self):
        assert self.is_disappeared (*ProductPageLocators.MESSAGE_OF_ADDING_BOOK_IN_BASKET), 'Сообщение о добавлении в корзину не появилось'