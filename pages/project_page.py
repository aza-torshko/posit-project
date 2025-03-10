from playwright.sync_api import Page

class ProjectPage:
    def __init__(self, page: Page):
        """Project Page Locators"""
        self.page = page
        self.ide_iframe = page.frame_locator("iframe#contentIFrame")
        self.console_tab_set_in_ide = self.ide_iframe.locator("//div[@aria-label='ConsoleTabSet']")
        self.project_name = page.locator("div#currentLocation")
        self.project_name_input = page.locator("div#currentLocation > input")
        self.project_title = page.locator("button.projectTitle")
        self.more_actions = page.locator("button.action.moreActions")
        self.perfrom_action = page.locator("button.action.delete")