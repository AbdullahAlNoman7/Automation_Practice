import pytest


@pytest.yield_fixture()
def browser_config():
    print('Browser launched..')
    yield
    print('Browser Closed..')


def test_login001(browser_config):
    print('Test Login..')


def test_home002(browser_config):
    print('Test home..')


def test_dashboard003(browser_config):
    print('Test dashboard')


def test_logout(browser_config):
    print('Test logout..')
