from playwright.sync_api import Page

class SpacePage:
    def __init__(self, page: Page):
        """Space Page Locators"""
        self.page = page
        self.space_name = page.locator("input#name")
        self.space_name_with_owner = page.locator("//div[@class='spaceNameWithOwner']")
        self.space_header_title = page.locator("div#headerTitle")
        self.space_more_actions = page.locator("//button[@aria-label='Automation Space: More Actions']")
        self.delete_space = page.locator("button#headerDeleteSpaceButton")
        self.delete_space_input = page.locator("input#deleteSpaceTest")
