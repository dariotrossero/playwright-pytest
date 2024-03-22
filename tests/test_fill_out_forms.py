from playwright.sync_api import Page
import allure
from pages.forms_page import FormsPage


class TestFillOutForms:

    @allure.title("Fill out form")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_fill_out_form(self, home_page, page: Page):
        home_page.click_fill_out_forms()
        forms_page = FormsPage(page)
        forms_page.enter_name("Pedro")
        forms_page.enter_message("This is a test message")
        forms_page.click_submit()
        assert not forms_page.captcha_error_displayed()
