import time

from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = r'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket_promo()
    time.sleep(2)
    product_page.is_product_in_basket_popups()

