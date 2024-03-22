from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class SignInPage(BasePage):
    _URL = BasePage.BASE_PATH + "/users/sign_in"
    _EMAIL_INPUT = {"role": "placeholder", "name": "Email"}
    _PASSWORD_INPUT = {"role": "placeholder", "name": "Password"}
    _SIGN_IN_BUTTON = {"role": "button", "name": "Sign in"}
    _ERROR_MESSAGE = "xpath=//p[text()='Invalid email or password.']"

    def __init__(self, page):
        self.page = page
        self.email_input = self.page.get_by_placeholder("Email")
        self.password_input = self.page.get_by_placeholder("Password")
        self.sign_in_button = self.page.get_by_role(**self._SIGN_IN_BUTTON)
        self.error_message = self.page.locator(self._ERROR_MESSAGE)

    def login(self, username: str, password: str) -> None:
        self.email_input.fill(username)
        self.password_input.fill(password)
        self.sign_in_button.click()

    def is_error_visible(self) -> bool:
        try:
            expect(self.error_message).to_be_visible(timeout=10000)
        except AssertionError:
            return False
        return True


