from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    # page.go_to_login_page()
    # login_page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/ru/accounts/login/')
    # login_page.should_be_login_page()
