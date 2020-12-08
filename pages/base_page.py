import selenium
import pytest
from selenium import webdriver


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

# pytest "C:\Users\D.ryzhenkov.HORATIO\Projects\Stepik_Selenium_Python\Stepik_mod_4\base_page.py" --browser_name=chrome -v --language=en
