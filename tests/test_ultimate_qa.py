import pytest

from pages.sing_in_page import SignInPage
from pages.ultimate_qa_page import UltimateQAPage
from playwright.sync_api import Page, expect


class TestUltimateQA:

    def test_login_fail(self, page: Page, home_page):
        home_page.click_login_automation_link()
        sign_in_page = SignInPage(page)
        sign_in_page.login("dario@dario.com", "pepe")
        assert sign_in_page.is_error_visible()
