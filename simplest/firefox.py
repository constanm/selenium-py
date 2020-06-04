from selenium import webdriver

from utils.configs import read_config

driver = webdriver.Firefox(executable_path=read_config()["paths"]["webdriver"]["geckodriver"])

driver.get("http://automationpractice.com/")

driver.quit()
