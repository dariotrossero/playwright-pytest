class BasePage:
    BASE_PATH = "https://ultimateqa.com"

    def open(self):
        self.page.goto(self._URL)
