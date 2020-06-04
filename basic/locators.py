from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.configs import geckodriver_path

driver = webdriver.Firefox(executable_path=geckodriver_path())
driver.get("http://automationpractice.com/")

# find_element
print("The WebElement with the ID 'search_query_top' is an <" +
      driver.find_element(By.ID, "search_query_top").tag_name + "> element")

# find_elements
elements = driver.find_elements_by_tag_name("input")
print("Found %s WebElements with the tag name <input> :" % len(elements))
# loop through all the elements and print their name
i = 1
for element in elements:
    print("element #" + str(i) + " is named '" + element.get_attribute("name") + "'")
    i += 1

# driver.find_element_by_xpath(xpath)
# driver.find_elements_by_xpath(xpath)
# driver.find_element_by_link_text(link_text)
# driver.find_elements_by_link_text(text)
# driver.find_element_by_partial_link_text(link_text)
# driver.find_elements_by_partial_link_text(link_text)
# driver.find_element_by_name(name)
# driver.find_elements_by_name(name)
# driver.find_element_by_tag_name(name)
# driver.find_elements_by_tag_name(name)
# driver.find_element_by_class_name(name)
# driver.find_elements_by_class_name(name)
# driver.find_element_by_css_selector(css_selector)
# driver.find_elements_by_css_selector(css_selector)
# driver.find_element(by=By.ID, value=None)
# driver.find_elements(by=By.ID, value=None)

driver.quit()
