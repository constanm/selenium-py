import unittest

from selenium import webdriver

from utils.configs import chromedriver_path


def setUpModule():
    """called once, before anything else in this module"""
    print('Starting module..')


def tearDownModule():
    """called once, after everything else in this module"""
    print('Stopping module..')


class RunChromeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setting up, once per class %s' % cls.__name__)
        cls.driver = webdriver.Chrome(executable_path=chromedriver_path())

    @classmethod
    def tearDownClass(cls):
        print('Tearing down, once per class %s' % cls.__name__)
        cls.driver.quit()

    def setUp(self):
        print('Setting up, before every test')
        self.driver.get("http://www.google.com")

    def tearDown(self):
        print('Tearing down, after every test')

    def test(self):
        print('Running test')
        self.driver.get("https://www.selenium.dev/")
        self.assertIn("Selenium", self.driver.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
