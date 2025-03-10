import pytest
from playwright.sync_api import expect
from actions.login_actions import LoginActions
from actions.space_actions import SpaceActions
from actions.project_actions import ProjectActions

def test_create_space_and_project(page):
    """Automates creating a new space, adding an RStudio project, and verifying IDE load."""
    login_actions = LoginActions(page)
    space_actions = SpaceActions(page)
    project_actions = ProjectActions(page)

    login_actions.navigate_to_posit_cloud()
    login_actions.login()

    # Create New Space
    space_actions.create_space("Automation Space")
    
    # Create a New RStudio Project within the Space
    project_actions.create_project("Automated RStudio By Aza")

    #Delete the RStudio Project
    project_actions.delete_project("Automated RStudio By Aza")

    #Delete the Space
    space_actions.delete_space("Automation Space")


    # page.click("button:has-text('New Project')")
    # page.click("button:has-text('RStudio')")

    # # Verifying that the RStudio IDE loads
    # page.wait_for_selector("iframe#contentIFrame", state="attached")
    # frame = page.frame_locator("iframe#contentIFrame")
    # assert frame is not None, "Iframe did not load"
    # frame.locator("//div[@aria-label='ConsoleTabSet']").wait_for()

    # page.wait_for_selector("div#currentLocation", state="visible")
    # page.locator("div#currentLocation").click()
    # page.fill("div#currentLocation > input", "Automated RStudio By Aza")
    # page.locator("div#currentLocation").press("Enter")
    # expect(page.locator("button.projectTitle")).to_have_text("Automated RStudio By Aza")
    
    # # Verifying RStudio iframe has title that matches the name that was given to the project
    # expect(page.locator('iframe[title="Automated RStudio By Aza"]')).to_be_visible()

    # #Delete the RStudio Project
    # page.locator("button.action.moreActions").click()
    # page.locator("button.action.delete").click()
    # page.locator("button:has-text('OK')").click()
    # expect(page.locator('iframe[title="Automated RStudio By Aza"]')).not_to_be_visible()
    # expect(page.locator("//div[text()='no content']")).to_be_visible()

    # #Delete the Space
    # page.locator("//button[@aria-label='Automation Space: More Actions']").click()
    # page.locator("button#headerDeleteSpaceButton").click()
    # page.locator("input#deleteSpaceTest").fill("Delete Automation Space")
    # page.get_by_role("button", name="Delete").click()
    # expect(page.locator("//div[@class='spaceNameWithOwner']")).not_to_be_visible()

