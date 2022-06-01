import pytest
from time import sleep
import logging

log = logging.getLogger(__name__)

# from playwright.sync_api import sync_playwright
# from playwright.sync_api import Page

# @pytest.fixture(scope='session')
# def playwright():
#     yield sync_playwright()

def page(playwright):
    webkit = playwright.webkit
    browser = webkit.launch()
    context = browser.new_context()
    page = context.new_page()
    yield page


@pytest.fixture
def pre_auth_page(playwright, pa_api_from_token, pyramid_settings):
    webkit = playwright.webkit
    browser = webkit.launch()
    context = browser.new_context()
    context.add_cookies([ {
        'name': 'PyramidAuth',
        'value': pa_api_from_token.token,
        'url': pyramid_settings.url,
        'httpOnly': True
    } ]
    )
    page = context.new_page()
    yield page


@pytest.fixture
def login(page, pyramid_settings):
    log.info(page)
    page.set_default_timeout(pyramid_settings.page_timeout)
    page.goto(pyramid_settings.pyramid_server_url)
    log.info(page)
    assert page.title() == "Pyramid"
    page.fill('#presented-username', pyramid_settings.pyramid_server_admin_user)
    page.fill('#password',pyramid_settings.pyramid_server_admin_password)
    log.info("submit login")
    page.click("#btnSubmit")
    # sleep(2)
    # should be logged in
    assert(page.locator("id=header-component-user-icon"))

    return page

