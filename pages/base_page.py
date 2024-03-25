class BasePage:
    BASE_PATH = "https://ultimateqa.com"

    def open(self, timeout=None):
        self.page.goto(self._URL, timeout=timeout)
