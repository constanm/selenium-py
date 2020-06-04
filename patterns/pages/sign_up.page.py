import logging

import patterns.util.custom_logger as cl
from patterns.pages.base_page import BasePage
from patterns.pages.login_page import LoginPage
from patterns.util.page_loader import require_loaded


class SignUp(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        driver.get("http://automationpractice.com/")

    # Locators
    _login_link = "Sign in"
    _search_box = "search_query_top"

    def navigate_to_login(self):
        self.element_click(self._login_link, locator_type="link")
        return LoginPage(self.driver)

    @require_loaded
    def search_for(self, search_term):
        element = self.get_element(self._search_box)
        element.send_keys(search_term)
        element.submit()
        return self
