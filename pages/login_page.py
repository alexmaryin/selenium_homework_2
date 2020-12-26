from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Folder *login* is missing in url!'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is missing!'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register form is missing!'

    def register_new_user(self, email, password):
        self.should_be_login_form()
        self.get_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.get_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.get_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        self.get_element(*LoginPageLocators.REGISTER_BUTTON).click()

