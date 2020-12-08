import time
import selenium
import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.main_page import MainPage




def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


# pytest "C:\Users\D.ryzhenkov.HORATIO\Projects\Stepik_mod_4\test_main_page.py" -v --tb=line
# --tb=line указывает, что нужно выводить только одну строку из лога каждого упавшего теста
