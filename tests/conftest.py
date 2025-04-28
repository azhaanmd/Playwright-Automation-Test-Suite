import pytest
from playwright.sync_api import APIRequestContext, Playwright, sync_playwright
from utils.constants import REQRES_BASE_URL

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright):
    request_context = playwright.request.new_context(base_url=REQRES_BASE_URL)
    yield request_context
    request_context.dispose()