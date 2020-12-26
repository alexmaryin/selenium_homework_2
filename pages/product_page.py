from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    product_name = None
    product_price = None

    def should_be_promo_url(self, promo):
        assert f'promo={promo}' in self.browser.current_url, 'Attribute promo is missed in url!'

    def should_present_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Add to basket form is missing!'

    def grub_product_name_and_price(self):
        product = self.get_element(*ProductPageLocators.PRODUCT_NAME)
        assert product is not None, 'Product name was not found on page!'
        self.product_name = product.text
        product_price = self.get_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price is not None, 'Product price was not found on page!'
        self.product_price = product_price.text

    def should_popup_add_to_basket(self):
        alerts_strong = [alert.text for alert in self.browser.find_elements(*ProductPageLocators.ALERT_MESSAGES)]
        # print(alerts_strong)   # for debug!
        assert self.product_name in alerts_strong, 'Success add to basket alert was not popup!'

    def should_popup_info_with_basket_total(self):
        alerts_info = [info.text for info in self.browser.find_elements(*ProductPageLocators.INFO_MESSAGES)]
        # print(alerts_info)          # for debug!
        assert self.product_price in alerts_info, 'Total price in basket should be equal to price of product!'

    def add_to_basket_promo(self, promo):
        self.should_be_promo_url(promo)
        self.grub_product_name_and_price()
        self.should_present_add_to_basket_btn()
        self.get_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def is_product_in_basket_popups(self):
        self.should_popup_add_to_basket()
        self.should_popup_info_with_basket_total()