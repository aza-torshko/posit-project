from playwright.sync_api import expect
from pages.login_page import LoginPage
from config.credentials import Credentials

class LoginActions:
    def __init__(self, page):
        """Initialize login actions with the page object."""
        self.page = page
        self.login_page = LoginPage(page)
        self.config = Credentials

    def navigate_to_posit_cloud(self):
        self.page.goto("https://posit.cloud/")

    def login(self):
        """Perform login action using Playwright locators."""
        email = self.config.get_email()
        password = self.config.get_password()
        self.login_page.login_link.click()
        expect(self.login_page.login_header).to_be_visible()
        expect(self.login_page.email_input).to_be_visible()
        self.login_page.email_input.click()
        self.login_page.email_input.fill(email)
        self.login_page.continue_button.click()
        expect(self.login_page.password_input).to_be_visible()
        self.login_page.password_input.fill(password)
        self.login_page.login_button.click()
        expect(self.login_page.current_username).to_have_text("Aza Torshko")