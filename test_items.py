import time
from selenium.common.exceptions import NoSuchElementException

link = r'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
link_bad = r'http://selenium1py.pythonanywhere.com/ru/catalogue/'
selector = '#add_to_basket_form > button'


def test_item_page_should_contain_add_basket_btn(browser):
    browser.get(link)
    time.sleep(2)
    try:
        browser.find_element_by_css_selector(selector)
    except NoSuchElementException:
        assert False, "Button Add to basket should be on this page!"
