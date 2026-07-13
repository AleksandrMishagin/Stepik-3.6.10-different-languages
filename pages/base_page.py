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

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators

class BasePage ():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get (self.url)

    # Находим и кликаем кнопку "Войти", переключаемся на окно с оповещением, принимаем его
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url) 
        #alert = self.browser.switch_to.alert
        #alert.accept()

    # Проверяем, что кнопка "Войти" присутствует
    def should_be_login_link (self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page (self):

        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True