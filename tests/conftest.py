import pytest
from playwright.sync_api import sync_playwright
from actions.login_actions import LoginActions
import os
from pytest_html import extras

def pytest_addoption(parser):
    """Allows passing custom CLI options like --headless"""
    parser.addoption("--headless", action="store_true", default=False, help="Run browser in headless mode")

@pytest.fixture(scope="session")
def browser(request):
    """Launch Playwright browser session-wide with optional headless mode."""
    headless_mode = request.config.getoption("--headless")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless_mode)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """Create a new page for each test."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Configure pytest-html report plugin."""
    config.option.htmlpath = "test_report.html"
    config.option.self_contained_html = True
