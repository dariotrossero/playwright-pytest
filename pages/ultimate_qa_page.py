from playwright.async_api import Page

from pages.base_page import BasePage


class UltimateQAPage(BasePage):
    _URL = BasePage.BASE_PATH + "/automation"
    _LOGIN_AUTOMATION_LINK = {"role": "link", "name": "Login automation"}
    _FORMS_LINK = {"role": "link", "name": "Fill out forms"}

    def __init__(self, page: Page):
        self.page = page

    def click_login_automation_link(self):
        self.page.get_by_role(**self._LOGIN_AUTOMATION_LINK).click()

    def click_fill_out_forms(self):
        self.page.get_by_role(**self._FORMS_LINK).click()
