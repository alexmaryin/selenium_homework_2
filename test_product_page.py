import time
from pages.product_page import ProductPage

link_shellcoders = r'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link_coders_at_work = r'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link_coders_at_work)
    product_page.open()
    product_page.add_to_basket_promo('newYear')
    product_page.is_product_in_basket_popups()

