from playwright.sync_api import Page

from pages.shadow_dom_page import ShadowDomPage


class TestShadowDomExample:

    def test_shadow_dom(self, page: Page):
        shadow_dom_page = ShadowDomPage(page)
        shadow_dom_page.open()
        shadow_dom_page.open_edit_menu()


