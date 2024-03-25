from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class DragAndDropExamplePage(BasePage):
    _URL = "https://www.w3schools.com/html/html5_draganddrop.asp"
    _IMAGE = "#div1 img"
    _DESTINATION_DIV = "#div2"

    def __init__(self, page: Page):
        self.page = page
        self.image = self.page.locator(self._IMAGE)
        self.destination_div = self.page.locator(self._DESTINATION_DIV)

    def drag_and_drop(self):
        self.image.drag_to(self.destination_div)

    def image_moved(self):
        return self.page.locator(self._DESTINATION_DIV + " img").is_visible()
