from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_info(self):
        assert self.is_element_not_present(*BasketPageLocators.PRODUCTS_IN_BASKET), 'Basket should be empty!'
