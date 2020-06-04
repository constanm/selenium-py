from selenium import webdriver
from selenium.webdriver import ActionChains

from utils.configs import chromedriver_path

with webdriver.Chrome(executable_path=chromedriver_path(), service_log_path=r"../chromedriver.log") as driver:
    # try accessing a hidden sub menu
    driver.get("http://automationpractice.com/index.php?controller=contact")
    menu = driver.find_element_by_css_selector(".sf-menu > li:nth-child(2) > a:nth-child(1)")
    ActionChains(driver).move_to_element(menu).perform()

    hidden_submenu = driver.find_element_by_css_selector(
        ".sf-menu > li:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)")
    ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

    # try some html5 drag-and-drop
    driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_draganddrop")
    # notice the switch_to frame!
    driver.switch_to.frame("iframeResult")

    source_element = driver.find_element_by_id("drag1")
    dest_element = driver.find_element_by_id("div1")

    # not working
    ActionChains(driver).drag_and_drop(source_element, dest_element).perform()

    # not working again
    ActionChains(driver).click_and_hold(source_element).move_to_element(dest_element).release(dest_element).perform()

    # working https://stackoverflow.com/a/53930565
    driver.execute_script(
        "function createEvent(typeOfEvent) {\n" + "var event =document.createEvent(\"CustomEvent\");\n"
        + "event.initCustomEvent(typeOfEvent,true, true, null);\n" + "event.dataTransfer = {\n" + "data: {},\n"
        + "setData: function (key, value) {\n" + "this.data[key] = value;\n" + "},\n"
        + "getData: function (key) {\n" + "return this.data[key];\n" + "}\n" + "};\n" + "return event;\n"
        + "}\n" + "\n" + "function dispatchEvent(element, event,transferData) {\n"
        + "if (transferData !== undefined) {\n" + "event.dataTransfer = transferData;\n" + "}\n"
        + "if (element.dispatchEvent) {\n" + "element.dispatchEvent(event);\n"
        + "} else if (element.fireEvent) {\n" + "element.fireEvent(\"on\" + event.type, event);\n" + "}\n"
        + "}\n" + "\n" + "function simulateHTML5DragAndDrop(element, destination) {\n"
        + "var dragStartEvent =createEvent('dragstart');\n" + "dispatchEvent(element, dragStartEvent);\n"
        + "var dropEvent = createEvent('drop');\n"
        + "dispatchEvent(destination, dropEvent,dragStartEvent.dataTransfer);\n"
        + "var dragEndEvent = createEvent('dragend');\n"
        + "dispatchEvent(element, dragEndEvent,dropEvent.dataTransfer);\n" + "}\n" + "\n"
        + "var source = arguments[0];\n" + "var destination = arguments[1];\n"
        + "simulateHTML5DragAndDrop(source,destination);", source_element, dest_element)

    # todo: rewrite this script as a proper test
