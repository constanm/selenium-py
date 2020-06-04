import unittest

from selenium import webdriver

from utils import configs


class ScreenshotTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=configs.chromedriver_path())
        self.driver.delete_all_cookies()
        # NOTE: In addCleanup, the first in, is executed last.
        self.addCleanup(self.driver.quit)
        self.addCleanup(self.screen_shot)
        self.driver.implicitly_wait(5)

    def screen_shot(self):
        """Take a Screen-shot of the drive homepage, when it Failed."""
        for method, error in self._outcome.errors:
            if error:
                self.driver.get_screenshot_as_file("screenshot-" + self.id() + ".png")

    def test_window_title_should_fail(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")
        # self.assertIn("Wrong Title!!!", driver.title)
