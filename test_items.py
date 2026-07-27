import time
from selenium.webdriver.common.by import By

def test_guest_should_see_add_to_basket_button(browser):
    # Ссылка на проверяемый товар
    link = "http://pythonanywhere.com"
    browser.get(link)

    # Обязательная пауза 30 секунд для визуальной проверки языка проверяющими
    time.sleep(30)

    # Поиск кнопки добавления в корзину по уникальному CSS-селектору класса
    buttons = browser.find_elements(By.CSS_CLASS_NAME, "btn-add-to-basket")

    # Проверяем, что кнопка найдена и присутствует на странице
    assert (len(buttons) > 0), "Кнопка добавления в корзину не найдена на странице!"
