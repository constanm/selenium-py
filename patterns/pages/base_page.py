from patterns.base.selenium_driver import SeleniumDriver
from traceback import print_stack
from patterns.util.utils import Util


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class
        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, title_to_verify):
        """
        Verify the page Title
        Parameters:
            title_to_verify: Title on the page that needs to be verified
        """
        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, title_to_verify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
