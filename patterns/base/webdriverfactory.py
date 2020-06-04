"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.get_instance()
"""
import logging

from selenium import webdriver

import patterns.util.custom_logger as logger
from patterns.errors.WdfError import WdfError
from utils import configs


class WebDriverFactory:
    log = logger.customLogger(logging.DEBUG)

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    def get_instance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        if self.browser == "iexplorer":
            # todo: make this work
            driver = webdriver.Ie()
            self.log.info("Running tests on Internet Explorer")
        elif self.browser == "firefox":
            self.log.info("Running tests on Firefox")
            driver = webdriver.Firefox(configs.geckodriver_path())
        elif self.browser == "chrome":
            self.log.info("Running tests on Chrome")
            driver = webdriver.Chrome(configs.chromedriver_path())
        else:
            raise WdfError("Unknown browser")
        # Setting Driver Implicit Time out in seconds for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()

        return driver
