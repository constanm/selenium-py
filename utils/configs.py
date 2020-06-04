import os

import yaml


def read_config():
    with open(os.path.join(os.path.dirname(__file__), "../config.yml")) as ymlfile:
        return yaml.load(ymlfile, Loader=yaml.BaseLoader)


def chromedriver_path():
    os.environ["webdriver.chrome.driver"] = read_config()["paths"]["webdriver"]["chromedriver"]
    return os.environ["webdriver.chrome.driver"]


def geckodriver_path():
    os.environ["webdriver.gecko.driver"] = read_config()["paths"]["webdriver"]["geckodriver"]
    return os.environ["webdriver.gecko.driver"]


def default_browser():
    return read_config()["browser"]
