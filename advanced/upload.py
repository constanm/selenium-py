import os
import time

from selenium import webdriver

from utils.configs import geckodriver_path

browser = webdriver.Firefox(executable_path=geckodriver_path(),
                            service_log_path=r"../geckodriver.log")
browser.get("http://automationpractice.com/index.php?controller=contact")

# try to upload this script
# NB: when using Remote Web Driver see 'file_detector' and 'LocalFileDetector'
script_path = os.path.realpath(__file__)
upload_element = browser.find_element_by_id("fileUpload")
upload_element.send_keys(script_path)

time.sleep(5)

browser.quit()
