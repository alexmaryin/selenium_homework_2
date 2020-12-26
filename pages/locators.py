from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_INVALID_LINK = (By.CSS_SELECTOR, '#lugin_link')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ALERT_MESSAGES = (By.CSS_SELECTOR, '#messages .alert-success strong')       # returns all success messages
    INFO_MESSAGES = (By.CSS_SELECTOR, '#messages .alert-info strong')           # returns all info messages


class BasketPageLocators:
    # this one selects all items in basket for list!
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
