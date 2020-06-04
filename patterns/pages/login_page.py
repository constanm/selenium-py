import logging

import patterns.util.custom_logger as cl
from patterns.pages.base_page import BasePage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _email_field = "email"
    _password_field = "passwd"
    _sign_in_button = "SubmitLogin"

    def enter_email(self, email):
        self.send_keys(email, self._email_field)
        return self

    def enter_password(self, password):
        self.send_keys(password, self._password_field)
        return self

    def click_sign_in_button(self):
        self.element_click(self._sign_in_button, locator_type="name")
        return self

    def login(self, email="", password=""):
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in_button()

    def verify_failed_login(self):
        result = self.is_element_present("//*[@id='center_column']/div[1]/ol/li", locator_type="xpath")
        return result

    # todo: implement this check
    def verify_successful_login(self):
        result = None
        return result

    def verify_login_title(self):
        return self.verifyPageTitle("Login - My Store")
