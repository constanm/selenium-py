from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait

from utils.configs import geckodriver_path

with webdriver.Firefox(executable_path=geckodriver_path()) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("http://google.com")
    driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    first_result = wait.until(presence_of_element_located((By.ID, "result-stats")))
    print(first_result.get_attribute("textContent"))

    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
                                                                           ElementNotVisibleException,
                                                                           ElementNotSelectableException])

    element = wait.until(element_to_be_clickable((By.PARTIAL_LINK_TEXT, "cheese")))

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    element.click()



