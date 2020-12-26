from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    product_name = None
    product_price = None

    def should_be_promo_url(self, promo):
        assert f'promo={promo}' in self.browser.current_url, 'Attribute promo is missed in url!'

    def should_present_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Add to basket form is missing!'

    # puts product name and its price to class properties introduced above
    def grub_product_name_and_price(self):
        product = self.get_element(*ProductPageLocators.PRODUCT_NAME)
        assert product is not None, 'Product name was not found on page!'
        self.product_name = product.text
        product_price = self.get_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price is not None, 'Product price was not found on page!'
        self.product_price = product_price.text

    # checks for presence of product name in list of alerts popup messages
    def should_popup_add_to_basket(self):
        alerts_strong = [alert.text for alert in self.browser.find_elements(*ProductPageLocators.ALERT_MESSAGES)]
        assert self.product_name in alerts_strong, 'Success add to basket alert was not popup!'

    # checks for presence of price of added product in list of info popup messages
    def should_popup_info_with_basket_total(self):
        alerts_info = [info.text for info in self.browser.find_elements(*ProductPageLocators.INFO_MESSAGES)]
        assert self.product_price in alerts_info, 'Total price in basket should be equal to price of product!'

    def should_not_be_success_message(self):
        assert self.is_element_not_present(*ProductPageLocators.ALERT_MESSAGES), \
            'Success message should not present on page!'

    def should_success_disappears(self):
        assert self.is_element_disappeared(*ProductPageLocators.ALERT_MESSAGES), \
            'Success message should disappear in 4 sec!'

    def add_to_basket_promo(self, promo):
        self.should_be_promo_url(promo)
        self.grub_product_name_and_price()
        self.should_present_add_to_basket_btn()
        self.get_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def add_to_basket(self):
        self.grub_product_name_and_price()
        self.should_present_add_to_basket_btn()
        self.get_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def is_product_in_basket_popups(self):
        self.should_popup_add_to_basket()
        self.should_popup_info_with_basket_total()
