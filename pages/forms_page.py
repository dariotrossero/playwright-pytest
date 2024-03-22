from playwright.sync_api import expect

from pages.base_page import BasePage


class FormsPage(BasePage):
    _URL = BasePage.BASE_PATH + "/filling-out-forms/"
    _CONTACT_NAME_INPUT = "//input[@id='et_pb_contact_name_1']"
    _MESSAGE_TEXT_AREA = "//textarea[@id='et_pb_contact_message_1']"
    _SUBMIT_BUTTON = "(//button[@name='et_builder_submit_button'])[2]"
    _CAPTCHA_INPUT = "input.et_pb_contact_captcha"

    def __init__(self, page):
        self.page = page
        self.contact_name_input = self.page.locator(self._CONTACT_NAME_INPUT)
        self.message_text_area = self.page.locator(self._MESSAGE_TEXT_AREA)
        self.submit_button = self.page.locator(self._SUBMIT_BUTTON)
        self.captcha_input = self.page.locator(self._CAPTCHA_INPUT)

    def click_submit(self):
        self.submit_button.click()

    def enter_name(self, name: str):
        self.contact_name_input.fill(name)

    def enter_message(self, message: str):
        self.message_text_area.fill(message)

    def captcha_error_displayed(self):
        try:
            expect(self.captcha_input).to_have_css("border", "1px solid rgb(255, 0, 0)")
        except AssertionError as e:
            # log exception
            return False
        return True

