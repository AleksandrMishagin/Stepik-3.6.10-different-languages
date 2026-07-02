import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Регистрируем новый параметр командной строки для pytest
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, fr, etc...")

# Создаем фикстуру, которая будет запускать браузер с нужным языком
@pytest.fixture(scope="function")
def browser(request):
    # Считываем значение параметра --language из командной строки
    user_language = request.config.getoption("language")
    
    print(f"\nstart chrome browser for test with language: {user_language}...")
    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    # Инициализируем браузер
    browser = webdriver.Chrome(options=options)
    
    yield browser
    
    # Закрываем браузер после завершения теста
    print("\nquit browser...")
    browser.quit()