import pytest

from patterns.base.webdriverfactory import WebDriverFactory


@pytest.yield_fixture()
def set_up():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def one_time_set_up(request, browser):
    print("Running one time setUp")
    # instantiate a WebDriver of the desired type
    driver = WebDriverFactory(browser).get_instance()

    if request.cls is not None:
        request.cls.driver = driver

    # pass it back to fixture user
    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    # to allow passing the type of browser from cmd line
    parser.addoption(
        "--browser", help="Supported browsers chrome, firefox")
    # to allow skipping of tests
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
