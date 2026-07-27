import time
from selenium.webdriver.common.by import By

def test_guest_should_see_add_to_basket_button(browser):
    # Ссылка на проверяемый товар
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Обязательная пауза 30 секунд для визуальной проверки языка проверяющими
    time.sleep(10)

    # Поиск кнопки добавления в корзину по уникальному CSS-селектору класса
    buttons = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")

    # Проверяем, что кнопка найдена и присутствует на странице
    assert (len(buttons) > 0), "Кнопка добавления в корзину не найдена на странице!"
