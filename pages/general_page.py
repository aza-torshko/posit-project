from playwright.sync_api import Page

class GeneralPage:
    def __init__(self, page: Page):
        """General Locators"""
        self.page = page

    def get_span_by_text(self, text: str):
        """Returns a locator for dynamic text span element """
        return self.page.locator(f"//span[text()='{text}']")

    def get_div_by_text(self, text: str):
        """Returns a locator for dynamic text div element """
        return self.page.locator(f"//div[text()='{text}']")
