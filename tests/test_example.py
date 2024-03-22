import re
from playwright.sync_api import Page, expect, Route


class TestBasic:

    def test_has_title(self, page: Page):
        page.goto("https://playwright.dev/")
        page.locator("xpath=/")
        # Expect a title "to contain" a substring.
        expect(page).to_have_title(re.compile("Playwright"))

    def test_get_started_link(self, page: Page):
        page.goto("https://playwright.dev/")

        # Click the get started link.
        page.locator("xpath=//a[text()='Get started']").click()

        # Expects page to have a heading with the name of Installation.
        expect(page.locator("xpath=//h1[text()='Installation']")).to_be_visible()

    def test_mock_the_fruit_api(self, page: Page):
        def handle(route: Route):
            json = [{"name": "Strawberry", "id": 21}, {"name": "Pineapple", "id": 22}]
            # fulfill the route with the mock data
            route.fulfill(json=json)

        # Intercept the route to the fruit API
        page.route("*/**/api/v1/fruits", handle)

        # Go to the page
        page.goto("https://demo.playwright.dev/api-mocking")

        # Assert that the Strawberry fruit is visible
        expect(page.get_by_text("Strawberry")).to_be_visible()
