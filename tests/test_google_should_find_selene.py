import pytest
from selene import browser, be, have


def test_google_search_success_result():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests'))


def test_google_search_empty_result():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('adsdqw34r2345243rtsdfvsd').press_enter()
    browser.element('[id="botstuff"]').should(have.text('ничего не найдено'))
