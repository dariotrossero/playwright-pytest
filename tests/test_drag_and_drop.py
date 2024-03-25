import pytest
from playwright.sync_api import Page

from pages.drag_and_drop_example_page import DragAndDropExamplePage


class TestDragAndDropExample:

    @pytest.fixture
    def drag_and_drop_page(self, page: Page):
        return DragAndDropExamplePage(page)

    def test_drag_n_drop(self, drag_and_drop_page):
        drag_and_drop_page.open(timeout=100000)
        drag_and_drop_page.drag_and_drop()
        assert drag_and_drop_page.image_moved()
