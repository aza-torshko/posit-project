from playwright.sync_api import expect
from actions.general_actions import GeneralActions
from pages.general_page import GeneralPage
from pages.project_page import ProjectPage

class ProjectActions:
    def __init__(self, page):
        """Initialize project actions with the page object"""
        self.page = page
        self.general_page = GeneralPage(page)
        self.project_page = ProjectPage(page)
        self.general_actions = GeneralActions(page)

    def create_rstudio_project(self, project_name):
        """Create New RStudio Project"""
        self.general_actions.click_button_by_span_text("New Project")
        self.general_actions.click_button_by_span_text("New RStudio Project")
        self.page.wait_for_selector("iframe#contentIFrame")
        # Giving a Name the project
        self.project_page.project_name.click()
        self.project_page.project_name_input.fill(project_name)
        self.project_page.project_name.press("Enter")
        # Verifying the project name is displayed
        expect(self.project_page.project_title).to_have_text(project_name)
        expect(self.project_page.project_name).to_be_visible(timeout=10000)

    def delete_project(self, project_name):
        """Delete Project"""
        self.project_page.more_actions.click()
        self.project_page.perfrom_action.click()
        self.general_actions.click_button_by_span_text("OK")
        # Verifying Success message that project was deleted 
        self.general_actions.verify_span_text("Success! Content has been trashed. It will be permanently deleted in 30 days.")
        # Project is not visible 
        expect(self.project_page.project_title).not_to_be_visible()
        self.general_actions.verify_div_text("no content")
