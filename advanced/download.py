import os
import time

from selenium import webdriver

from utils.configs import read_config

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/java-archive")

browser = webdriver.Firefox(firefox_profile=fp,
                            executable_path=read_config()["paths"]["webdriver"]["geckodriver"],
                            service_log_path=r"../geckodriver.log")
browser.get("https://www.selenium.dev/downloads/")
# try to dowload version 3.x
browser.find_element_by_partial_link_text("3.").click()

time.sleep(10)

browser.quit()
