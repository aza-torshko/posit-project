from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        """Initialize login locators"""
        self.page = page
        self.login_link = page.locator("//a/span[text()='Log In']")
        self.login_header = page.locator("//h2/span['Log In']")
        self.email_input = page.get_by_role("textbox", name="Email")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Log in")
        self.current_username = page.locator("//button[@id='currentUser']//div[@class='userName']")
