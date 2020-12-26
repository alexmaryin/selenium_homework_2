import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # opens browser with link from constructor
    def open(self):
        self.browser.get(self.url)

    # return true if element is present on page
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # return element on page if present
    def get_element(self, how, what):
        if self.is_element_present(how, what):
            return self.browser.find_element(how, what)
        else:
            return None

    # return true if element is not present on page
    def is_element_not_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # return true if element is disappear from page before timeout
    def is_element_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException)\
                .until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # goes to login page
    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    # goes to basket page
    def go_to_basket(self):
        self.should_be_basket_link()
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    # check for login link available
    def should_be_login_link(self):
        self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login links is missed!'

    # check for basket link available
    def should_be_basket_link(self):
        self.is_element_present(*BasePageLocators.BASKET_LINK), 'Basket link is missed!'

    # super bot-driven captcha resolver
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
