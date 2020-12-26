import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage

link_index = r'http://selenium1py.pythonanywhere.com/'


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link_index)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link_index)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
