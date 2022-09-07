from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginScreen:
    EMAIL_FIELD = (By.ID, "email")
    EMAIL_FIELD_TITLE = (By.CSS_SELECTOR, "[data-qa-id='email-input-label']")
    PASSWORD_FIELD = (By.ID, "password")
    PASSWORD_FIELD_TITLE = (By.CSS_SELECTOR, "[data-qa-id='password-input-label']")
    LOGIN_BUTTON = (By.ID, "logIn")
    LANDING_PAGE_HOME_BUTTON = (By.CLASS_NAME, "hui-globalnav__home-logo")
    BACK_BUTTON = (By.CLASS_NAME, "styles_backIcon_1nBYGKhbTIbTmIULDJg1MZ")
    NEED_HELP_LINK = (By.CSS_SELECTOR, "[data-qa-id='need-help-link']")
    HULD_LOGO = (By.CSS_SELECTOR, "[data-qa-id='hudl-logo']")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")
    LOGIN_WITH_ORG_BTN = (By.CSS_SELECTOR, "[data-qa-id='log-in-with-organization-btn']")
    REMEMBER_ME_CHECKBOX_LABEL = (By.CSS_SELECTOR, "[data-qa-id='remember-me-checkbox-label']")
    REMEMBER_ME_CHECKBOX = (By.CLASS_NAME, "uni-form__check-item")
    USR_NAME_PASSWORD_ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-qa-id='error-display']")
    NEED_HELP_ERROR_MESSAGE_LINK = (By.LINK_TEXT, "Need help?")
    RESET_PASSWORD_TITLE = (By.CSS_SELECTOR, "[data-qa-id='lets-reset-password-headline']")
    LOG_INTO_HUDL_WITH_ORG_EMAIL = (By.CLASS_NAME,
                                    "uni-headline uni-headline--2 uni-padding--one _3ZchjyyL4lRtJSkmDHSLIy")
    LOG_INTO_HUDL_WITH_ORG_EMAIL_FIELD_TEXT = (By.CLASS_NAME, "uni-text")
    LOGIN_PAGE_EXPECTED_ELEMENTS = [EMAIL_FIELD, EMAIL_FIELD_TITLE, PASSWORD_FIELD, PASSWORD_FIELD_TITLE, LOGIN_BUTTON,
                                    BACK_BUTTON, NEED_HELP_LINK, HULD_LOGO, SIGNUP_LINK, LOGIN_WITH_ORG_BTN,
                                    REMEMBER_ME_CHECKBOX_LABEL, REMEMBER_ME_CHECKBOX]

    def __init__(self, driver):
        self.driver = driver

    def is_present(self, element, timeout=10):
        return WebDriverWait(self.driver, timeout=timeout).until(ec.presence_of_element_located(element)) \
               and WebDriverWait(self.driver, timeout=timeout).until(ec.visibility_of_element_located(element))

    def click(self, element):
        element = self.is_present(element).click()

    def type(self, element, text):
        element = self.is_present(element).send_keys(text)