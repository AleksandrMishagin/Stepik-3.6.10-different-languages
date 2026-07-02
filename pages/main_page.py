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

from .base_page import BasePage

class MainPage(BasePage):
    
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()