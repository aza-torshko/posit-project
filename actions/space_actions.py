from playwright.sync_api import expect
from actions.general_actions import GeneralActions
from pages.general_page import GeneralPage
from pages.space_page import SpacePage

class SpaceActions:
    def __init__(self, page):
        """Initialize space actions with the page object."""
        self.page = page
        self.general_actions = GeneralActions(page)
        self.general_page = GeneralPage(page)
        self.space_page = SpacePage(page)

    def create_space(self, space_name):
        """Create New Space"""
        self.general_actions.click_button_by_span_text("New Space")
        self.space_page.space_name.fill(space_name)
        self.general_actions.click_button_by_span_text("Create")
        # Verifying the space with given name is displayed
        expect(self.space_page.space_header_title).to_have_text(space_name)

    def delete_space(self, space_name):
        """Delete Space"""
        # Since the accoiunt can have only one space, at the end of each test the space should be deleted
        self.space_page.space_more_actions.click()
        self.space_page.delete_space.click()
        self.space_page.delete_space_input.fill("Delete " + space_name)
        self.general_actions.click_button_by_span_text("Delete")
        # Verifying the space was deleted
        self.general_actions.verify_span_text(f'Success! The space "{space_name}" has been deleted.')
        expect(self.space_page.space_name_with_owner).not_to_be_visible()

        
