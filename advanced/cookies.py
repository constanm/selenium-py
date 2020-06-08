import json

from selenium import webdriver

from utils.configs import chromedriver_path

with webdriver.Chrome(executable_path=chromedriver_path(), service_log_path=r"../chromedriver.log") as driver:
    driver.get("http://www.example.com")

    # Adds the cookie into current browser context
    driver.add_cookie({"name": "key", "value": "value"})

    # Get cookie details with named cookie 'foo'
    print(driver.get_cookie("foo"))

    # Get cookie details with named cookie 'foo'
    print(driver.get_cookie("key"))

    driver.add_cookie({"name": "test1", "value": "cookie1"})
    driver.add_cookie({"name": "test2", "value": "cookie2"})

    # Get all available cookies
    print(json.dumps(driver.get_cookies(), sort_keys=True, indent=4))

    # Delete a cookie with name 'test1'
    driver.delete_cookie("test1")

    #  Deletes all cookies
    driver.delete_all_cookies()

    # Get all available cookies
    print(json.dumps(driver.get_cookies(), sort_keys=True, indent=4))
