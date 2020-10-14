import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import FirefoxProfile

# Указаны обязательные параметры запуска browser и language
# Для формального прохождения задания дефолтный браузер указан chrome
# чтобы команда pytest --language=es test_items.py не вернула эксепшен
# Таким образом, параметр browser сделал для теста не обязательным


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru, es, fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    lng = request.config.getoption("language")
    # проверяется указание в командной строке параметра запуска --language
    if not lng:
        raise pytest.UsageError("--language={en|ru|fr|es}")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # печать указанного при запуске параметра language не делал
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lng})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", lng)
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name={chrome|firefox}")
    yield browser
    print("\nquit browser..")
    browser.quit()
