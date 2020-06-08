import unittest

import pytest

from patterns.pages.home_page import HomePage


# Run from command line
# python -m pytest patterns/tests/test_login.py --browser chrome

@pytest.mark.usefixtures("one_time_set_up", "set_up")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, one_time_set_up):
        self.home_page = HomePage(self.driver)

    @pytest.mark.slow
    def test_valid_login(self):
        self.home_page = HomePage(self.driver)
        login_page = self.home_page.navigate_to_login()
        # use credentials from sign up test
        page = login_page.enter_email("some_email@email.com").enter_password("correct_password").click_sign_in_button()
        assert page.get_title() == "My Store"

    def test_invalid_login(self):
        self.home_page = HomePage(self.driver)
        login_page = self.home_page.navigate_to_login()
        page = login_page.enter_email("some_email@email.com").enter_password("wrong_password").click_sign_in_button()
        assert page.get_title() == "Login - My Store"
