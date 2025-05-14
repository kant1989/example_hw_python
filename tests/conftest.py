import pytest
from selene import browser
from selenium import webdriver
import project_config


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.base_url = project_config.config.base_url
    browser.config.window_height = project_config.config.window_height
    browser.config.window_width = project_config.config.window_width
    browser.config.driver_name = project_config.config.driver_name
    browser.config.timeout = project_config.config.timeout
    if project_config.config.headless:
        if browser.config.driver_name == 'chrome':
            driver_options = webdriver.ChromeOptions()
        elif browser.config.driver_name == 'firefox':
            driver_options = webdriver.FirefoxOptions()
        elif browser.config.driver_name == 'edge':
            driver_options = webdriver.EdgeOptions()
        driver_options.add_argument('--headless=new')
        browser.config.driver_options = driver_options
    yield
    browser.quit()
