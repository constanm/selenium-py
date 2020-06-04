import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.configs import chromedriver_path


class JavascriptTests(unittest.TestCase):

    driver = None

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
        self.driver.get("http://automationpractice.com/")

    def tearDown(self):
        print('Tearing down, after every test')

    def test_scroll_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def test_scroll_to_element(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.execute_script("document.getElementById(\"search_query_top\").scrollIntoView();")

    def test_click_element(self):
        # using By.* locator
        submit_search_button = self.driver.find_element(By.NAME, "submit_search")
        self.driver.execute_script("arguments[0].click();", submit_search_button)

        # wait to load results
        time.sleep(5)

        # chaining of find_element_by*
        p_results = self.driver.find_element_by_xpath("//*[@id=\"center_column\"]").find_element_by_tag_name("p")
        self.assertIn("Please enter a search key", p_results.text)

    def test_enable_disable_element(self):
        button = self.driver.find_element(By.NAME, "submit_search")
        self.driver.execute_script("arguments[0].click();", button)

        # wait to load results
        time.sleep(5)

        # re-read the element after action to avoid Stale Element Exceptions
        button = self.driver.find_element(By.NAME, "submit_search")

        self.assertTrue(button.is_enabled())
        self.driver.execute_script("arguments[0].disabled = true;", button)
        self.assertFalse(button.is_enabled())
        self.driver.execute_script("arguments[0].disabled = false;", button)
        self.assertTrue(button.is_enabled())

    def test_set_and_read_hidden(self):
        hidden_element = self.driver.find_element_by_name("orderby")
        self.assertEqual("position", hidden_element.get_attribute("value"))
        self.driver.execute_script("arguments[0].setAttribute('value', 'price');", hidden_element)
        self.assertEqual("price", hidden_element.get_attribute("value"))

    def test_inner_html(self):
        element = self.driver.find_element_by_class_name("shop-phone")
        html = self.driver.execute_script("return arguments[0].innerHTML;", element)
        self.assertIn("0123-456-789", html)

    def test_pasting_long_text(self):
        self.driver.find_element_by_link_text("Contact us").click()
        time.sleep(5)

        long_text = ''.join(["*" for _ in range(500)])
        self.driver.find_element_by_id("message").send_keys(long_text)
        self.driver.execute_script("document.getElementById('message').value = arguments[0];", long_text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
