import random
import string
import pytest
from pages.BasketPage import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

link_index_page = r'http://selenium1py.pythonanywhere.com/'
link_product_no_promo = r'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
link_product_promo = r'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link_product_no_available = r'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
promo_links_group = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.login_guest
class TestLoginFromProductPage:

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link_product_no_promo)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link_product_no_promo)
        page.open()
        page.go_to_login_page()


@pytest.mark.product_page_test
class TestProductPageAsGuest:

    def test_guest_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link_product_no_promo)
        product_page.open()
        product_page.add_to_basket()
        product_page.is_product_in_basket_popups()

    def test_guest_can_add_new_year_promo_product_to_basket(self, browser):
        product_page = ProductPage(browser, link_product_promo)
        product_page.open()
        product_page.add_to_basket_promo(promo='newYear')
        product_page.is_product_in_basket_popups()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, link_product_no_promo)
        product_page.open()
        product_page.add_to_basket()
        product_page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link_product_no_promo)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, link_product_no_promo)
        product_page.open()
        product_page.add_to_basket()
        product_page.should_success_disappears()

    # Turn off for prevent waste of time of dear reviewers
    @pytest.mark.parametrize('link', promo_links_group)
    @pytest.mark.skip
    def test_guest_can_add_spec_promo_product_to_basket(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket_promo(link.partition('promo=')[2])
        product_page.is_product_in_basket_popups()


@pytest.mark.user_tests
class TestProductPageAsUser:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.email = ''.join(random.sample(string.ascii_lowercase, 10)) + "@fakemail.org"
        self.password = ''.join(random.sample(string.ascii_letters+string.digits, 10))
        page = LoginPage(browser, link_index_page)
        page.open()
        page.go_to_login_page()
        page.should_be_login_page()
        print(f'Trying register new user with email {self.email} and password {self.password}...')
        page.register_new_user(self.email, self.password)
        page.should_be_authorized_user()
        print('OK!\n')

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link_product_no_promo)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link_product_no_promo)
        product_page.open()
        product_page.add_to_basket()
        product_page.is_product_in_basket_popups()


@pytest.mark.basket_page_test
class TestBasketFromProductPage:

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        product_page = BasketPage(browser, link_product_no_promo)
        product_page.open()
        product_page.go_to_basket()
        product_page.should_be_empty_basket_info()
