import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help="Choose language: ru, en, fr, etc...")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    
    # Проверяем, что передан именно chrome, так как firefox мы пока убрали
    if browser_name == "chrome":
        print(f"\nstart chrome browser for test with language: {user_language}...")
        
        # Ваши добавленные строки конфигурации Chrome
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--browser_name currently supports only 'chrome'")
    
    yield browser

    print("\nquit browser...")
    browser.quit()