from playwright.sync_api import Page

from pages.base_page import BasePage


class ShadowDomPage(BasePage):

    _URL = "https://www.htmlelements.com/demos/menu/shadow-dom/index.htm"
    _MENU_ITEM = ".smart-ui-component:nth-child(1) div.smart-menu-item-label-element"

    def __init__(self, page: Page):
        self.page = page
        self.edit_menu = page.locator(self._MENU_ITEM).filter(has_text='Edit')
        self.view_menu = page.locator(self._MENU_ITEM).filter(has_text='View')

    def open_edit_menu(self):
        self.edit_menu.click()
        self.page.get_by_label("Redo").click()
