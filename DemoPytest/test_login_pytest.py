import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.yield_fixture()
def browser_config():
    global driver
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(5)

    yield
    time.sleep(3)
    driver.close()


def test_login001(browser_config):
    userName = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    btn_click = driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button')
    userName.send_keys('Admin')
    password.send_keys('admin123')
    btn_click.click()


@pytest.mark.order(1)
def test_login002_invalid(browser_config):
    userName = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    btn_click = driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button')
    userName.send_keys('Adminm')
    password.send_keys('admin123m')
    btn_click.click()


@pytest.mark.skip('Not ready yet')
def test_login002_invalid(browser_config):
    userName = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    btn_click = driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button')
    userName.send_keys('Adminm')
    password.send_keys('admin123m')
    btn_click.click()

@pytest.mark.order(2)
@pytest.mark.invalid
def test_login002_invalid(browser_config):
    userName = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    btn_click = driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button')
    userName.send_keys('Adminm')
    password.send_keys('admin123m')
    btn_click.click()
    expected_text = 'Invalid credentials'

@pytest.mark.order(3)
@pytest.mark.invalid
def test_login002_invalid(browser_config):
    userName = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    btn_click = driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button')
    userName.send_keys('Adminm')
    password.send_keys('admin123m')
    btn_click.click()


def test_home001_valid(browser_config):
    userName = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    btn_click = driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button')
    userName.send_keys('Admin')
    password.send_keys('admin123')
    btn_click.click()
