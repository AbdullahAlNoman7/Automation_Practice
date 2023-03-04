import pytest


def test_login():
    print('Test Login..')


@pytest.mark.order(2)
def test_home():
    print('Test home..')


@pytest.mark.order(1)
def test_dashboard():
    print('Test dashboard')


def test_logout():
    print('Test logout..')
