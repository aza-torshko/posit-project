from playwright.sync_api import expect
from pages.general_page import GeneralPage


class GeneralActions:
    def __init__(self, page):
        """Initialize login actions with the page object."""
        self.page = page
        self.general_page = GeneralPage(page)

    def click_button_by_span_text(self, span_text: str):
        """Clicks a button that contains a span with the given text."""
        button_locator = self.general_page.get_span_by_text(span_text)
        button_locator.click()
    
    def verify_div_text(self, expected_text):
        """Verify that a specific div contains the expected text"""
        div_locator = self.general_page.get_div_by_text(expected_text)
        expect(div_locator).to_have_text(expected_text)
    
    def verify_span_text(self, expected_text):
        """Verify that a specific div contains the expected text"""
        span_locator = self.general_page.get_span_by_text(expected_text)
        expect(span_locator).to_have_text(expected_text)