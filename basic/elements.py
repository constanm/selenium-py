from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

from utils.configs import geckodriver_path
from utils.configs import read_config

with webdriver.Firefox(executable_path=geckodriver_path()) as driver:
    paths_screenshots = read_config()["paths"]["screenshots"]
    wait = WebDriverWait(driver, 10)
    driver.get("http://google.com")
    q = driver.find_element(By.NAME, "q")

    # optionally switch to active element
    title = driver.switch_to.active_element.get_attribute("title")
    print("q's title is '%s'" % title)

    print("q's tag name is '%s', text is '%s'" % (q.tag_name, q.text))
    print("q's class is '%s'" % q.get_attribute("class"))
    print("q's type is '%s'" % q.get_property("type"))

    q.click()

    print("q is displayed '%s'" % q.is_displayed())
    print("q is enabled '%s'" % q.is_enabled())
    # used mostly with checkboxes and radio buttons
    print("q is selected '%s'" % q.is_selected())

    q.send_keys("milk")
    q.screenshot(paths_screenshots + "/milk_was_searched.png")

    q.clear()

    q.send_keys("cheese")
    q.screenshot(paths_screenshots + "/cheese_was_searched.png")

    # q.submit()
    q.send_keys(Keys.RETURN)

    wait.until(presence_of_element_located((By.NAME, "q"))) \
        .screenshot(paths_screenshots + "/cheese_results.png")
