import pytest
from playwright.sync_api import expect
from actions.login_actions import LoginActions
from actions.space_actions import SpaceActions
from actions.project_actions import ProjectActions
from pages.space_page import SpacePage
from pages.project_page import ProjectPage

def test_create_space_and_project(page):
    """Creating a new space, adding an RStudio project, and verifying IDE loads"""
    login_actions = LoginActions(page)
    space_actions = SpaceActions(page)
    project_actions = ProjectActions(page)
    space_page = SpacePage(page)
    project_page = ProjectPage(page)

    #Login to account 
    login_actions.navigate_to_posit_cloud()
    login_actions.login()

    # Create New Space
    space_actions.create_space("Automation Space")
    expect(space_page.space_name_with_owner).to_have_text("Automation Space")
    expect(space_page.space_header_title).to_have_text("Automation Space")

    # Create New RStudio Project within the Space
    project_actions.create_rstudio_project("Automated RStudio By Aza")
    # Verifying that the RStudio IDE loads
    page.wait_for_selector("iframe#contentIFrame")
    # Verifying the element inside IDE loaded
    expect(project_page.console_tab_set_in_ide).to_be_visible(timeout=50000)

    #Delete the RStudio Project and Space 
    project_actions.delete_project("Automated RStudio By Aza")
    space_actions.delete_space("Automation Space")