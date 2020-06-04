import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

from utils import configs


class WebdriverTests(unittest.TestCase):

    def setUp(self):
        # when speed is not a factor is best to use a new instance. see test parallelization and test isolation
        self.driver = webdriver.Chrome(executable_path=configs.chromedriver_path())

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()

    def test_window_title(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")
        self.assertIn("My Store", driver.title)

    def test_page_source(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")
        self.assertIn("robots", driver.page_source)

    def test_current_url(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")
        self.assertIn("http://automationpractice.com/index.php", driver.current_url)

    def test_current_url(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")
        self.assertIn("index.php", driver.current_url)

    def test_desired_capabilities(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")
        self.assertIn("timeouts", driver.desired_capabilities)

    def test_window_sizing_and_moving(self):
        # not going to need original window thus minimizing it right away
        self.driver.minimize_window()

        # going to create my own window with my own options
        options = Options()
        options.add_argument("window-size=800,600")
        driver = webdriver.Chrome(options=options,
                                  executable_path=configs.chromedriver_path(),
                                  service_args=["--log-path=../chromedriver.log"])
        driver.get("http://automationpractice.com/")
        current_position = driver.get_window_rect()
        print("Window size: width = {}px, height = {}px".format(current_position["width"], current_position["height"]))
        print("Window position: X = {}, Y = {}".format(current_position["x"], current_position["y"]))
        time.sleep(1)

        driver.set_window_size(600, 400)
        size = driver.get_window_size()
        print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))
        time.sleep(1)

        driver.set_window_position(10, 10)
        time.sleep(1)

        driver.set_window_position(-100, -100)
        time.sleep(1)
        coordinates = driver.get_window_rect()
        print("Window position: X = {}, Y = {}".format(coordinates["x"], coordinates["y"]))

        driver.set_window_position(100, 100)
        time.sleep(1)

        driver.minimize_window()
        time.sleep(1)
        size = driver.get_window_size()
        print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))

        driver.maximize_window()
        time.sleep(1)
        size = driver.get_window_size()
        print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))

    def test_window_switching(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")

        current_window = driver.current_window_handle
        print("Current window handle " + current_window)

        # open a new window/tab
        driver.find_element_by_partial_link_text("Ecommerce software").click()
        time.sleep(1)

        # read all open windows/tabs
        window_handles = driver.window_handles
        first_tab = window_handles[0]
        last_tab = window_handles[1]

        # check we are on the still on first window/tab
        assert current_window == first_tab

        # reposition on the first
        driver.switch_to.window(first_tab)
        time.sleep(1)

        # reposition on the last
        driver.switch_to.window(last_tab)
        time.sleep(1)

        print("New window handle " + last_tab)
        time.sleep(1)

        # close the last
        driver.close()
        time.sleep(1)

        # switching to initial window/tab
        driver.switch_to.window(first_tab)
        time.sleep(1)

        assert driver.title == "My Store"

    def test_headless_mode(self):
        # closing original window
        self.driver.close()
        self.driver.quit()

        options = Options()
        options.add_argument(configs.read_config()["headless"])
        options.add_argument("window-size=800,600")
        driver = webdriver.Chrome(options=options,
                                  executable_path=configs.chromedriver_path(),
                                  service_args=["--log-path=../chromedriver.log"])
        self.driver = driver
        driver.get("http://google.com/")
        print(driver.get_window_size())
        self.assertIn("Google", driver.title)

    def test_navigation(self):
        driver = self.driver
        driver.get("http://google.com")
        driver.back()
        driver.refresh()
        driver.forward()
        self.assertIn("Google", driver.title)

    def test_select_element(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php?controller=contact")
        web_element = driver.find_element_by_id("id_contact")
        select_element = Select(web_element)
        time.sleep(1)
        select_element.select_by_index(1)
        time.sleep(1)
        select_element.select_by_value("2")
        time.sleep(1)
        select_element.select_by_visible_text("Webmaster")
        time.sleep(1)

        self.assertFalse(select_element.is_multiple)


if __name__ == "__main__":
    unittest.main()
