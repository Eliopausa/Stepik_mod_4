import time
import selenium


link = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)


# pytest "C:\Users\D.ryzhenkov.HORATIO\Projects\Stepik_mod_4\test_main_page.py" -v --tb=line
# --tb=line указывает, что нужно выводить только одну строку из лога каждого упавшего теста
