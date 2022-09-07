import time
import unittest
from LoginScreen import LoginScreen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginTestCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.hudl.com/login")
        self.wait = WebDriverWait(self.driver, timeout=10)
        self.login_screen = LoginScreen(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_screen_elements_of_login_screen(self):
        expected_elements = self.login_screen.LOGIN_PAGE_EXPECTED_ELEMENTS

        for element in expected_elements:
            self.login_screen.is_present(element)

    def test_successful_login(self):
        # insert provided username
        self.login_screen.type(self.login_screen.EMAIL_FIELD, "")
        self.login_screen.click(self.login_screen.PASSWORD_FIELD)
        # insert provided password
        self.login_screen.type(self.login_screen.PASSWORD_FIELD, "")
        self.login_screen.click(self.login_screen.LOGIN_BUTTON)

        self.login_screen.is_present(self.login_screen.LANDING_PAGE_HOME_BUTTON)

    def test_unsuccessful_login(self):
        # error message can be triggered without having to input any username or password
        self.login_screen.click(self.login_screen.LOGIN_BUTTON)

        error_message = self.login_screen.is_present(self.login_screen.USR_NAME_PASSWORD_ERROR_MESSAGE)
        assert error_message.text == "We didn't recognize that email and/or password.Need help?"
        self.wait.until(ec.element_to_be_clickable(self.login_screen.NEED_HELP_ERROR_MESSAGE_LINK))

    def test_password_reset_button(self):
        self.login_screen.click(self.login_screen.NEED_HELP_LINK)

        reset_password_title = self.login_screen.is_present(self.login_screen.RESET_PASSWORD_TITLE)
        assert reset_password_title.text == "Let’s reset your password"

    def test_login_screen_signup_button(self):
        self.login_screen.click(self.login_screen.SIGNUP_LINK)

        self.wait.until(ec.url_matches("https://www.hudl.com/register/signup"))

    def test_login_with_org_button(self):
        self.login_screen.click(self.login_screen.LOGIN_WITH_ORG_BTN)

        login_with_org_email_page_email_field_text = \
            self.login_screen.is_present(self.login_screen.LOG_INTO_HUDL_WITH_ORG_EMAIL_FIELD_TEXT)
        assert login_with_org_email_page_email_field_text.text == "Enter the email address used for your organisation"


if __name__ == "__main__":
    unittest.main()
