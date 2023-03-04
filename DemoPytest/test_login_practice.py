import time
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains


@pytest.yield_fixture()
def browser_setup():
    global driver
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get('https://www.startech.com.bd/')
    driver.implicitly_wait(5)

    yield
    time.sleep(2)
    print(driver.title)


@pytest.mark.skip('not needed..')
@pytest.mark.order(1)
def test_login001(browser_setup):
    clk_login = driver.find_element(By.CSS_SELECTOR, '.ac-content > p > a:nth-of-type(2)')
    clk_login.click()
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    clk_btn = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
    if username.is_enabled() == True and username.is_displayed() == True:
        username.send_keys('sagor@gmail.com')
    if password.is_selected() != True and password.is_enabled() == True:
        password.send_keys('123456')
    clk_btn.click()


@pytest.mark.skip('not need at this moment...')
def test_add_address():
    clk_edit = driver.find_element(By.CSS_SELECTOR, 'div:nth-of-type(2) > .ico-btn')
    clk_edit.click()
    add_address = driver.find_element(By.CSS_SELECTOR, '.ac-navbar .nav-item:nth-of-type(4) .nav-link')
    add_address.click()
    new_address = driver.find_element(By.CSS_SELECTOR, '.add-new.card > span:nth-of-type(2)')
    new_address.click()
    # Edit profile
    first_name = driver.find_element(By.NAME, 'firstname')
    last_name = driver.find_element(By.NAME, 'lastname')
    company = driver.find_element(By.NAME, 'company')
    address_01 = driver.find_element(By.NAME, 'address_1')
    address_02 = driver.find_element(By.NAME, 'address_2')
    city = driver.find_element(By.NAME, 'city')
    postcode = driver.find_element(By.NAME, 'postcode')
    country = driver.find_element(By.ID, 'input-country')
    region = driver.find_element(By.ID, 'input-zone')
    default_yes = driver.find_element(By.XPATH, '//input[@value="1"]')
    add = driver.find_element(By.CSS_SELECTOR, "form[method='post'] > .btn.btn-primary")
    # Add info
    first_name.send_keys('Md. ')
    last_name.send_keys('Ketty ')
    company.send_keys('SJ company China')
    address_01.send_keys('Dhaka bangladesh ')
    address_02.send_keys('Dhaka mirpur ')
    city.send_keys('Uttara ')
    postcode.send_keys('2104')
    sel_country = Select(country)
    # sel_country.deselect_by_value('18')
    sel_country.select_by_value('2')
    sel_region = Select(region)
    # all_option_region = sel_region.options
    for Allregion in sel_region.options:
        print('Value of...', Allregion.text)
        if Allregion.text == 'Tepelene':
            Allregion.click()
            break
    # sel_region.select_by_value('2')
    assert default_yes.is_displayed() == True
    default_yes.click()
    add.click()


@pytest.mark.order(2)
def test_search_item(browser_setup):
    driver.find_element(By.CSS_SELECTOR, ".brand > img[alt='Star Tech & Engineering Ltd ']").click()
    laptop = driver.find_element(By.CSS_SELECTOR, '.navbar-nav > li:nth-of-type(2) > .nav-link')
    gaming_laptop = driver.find_element(By.CSS_SELECTOR,
                                        'li:nth-of-type(2) > .drop-down.drop-menu-1 > li:nth-of-type(2) > .nav-link')
    razer = driver.find_element(By.CSS_SELECTOR,
                                'li:nth-of-type(2) > .drop-down.drop-menu-1 > li:nth-of-type(2) > '
                                '.drop-down.drop-menu-2 > li:nth-of-type(1) > .nav-link')
    action = ActionChains(driver)
    action.move_to_element(laptop).pause(2).move_to_element(gaming_laptop).pause(2).click(razer).pause(
        2).release().perform()
    select_laptop = driver.find_element(By.CSS_SELECTOR, '.main-content.p-items-wrap > div:nth-of-type(1) h4 > a')
    select_laptop.click()
    payment_month = driver.find_element(By.XPATH,
                                        "/html//div[@id='product']//label[@class='p-wrap']/span[@class='price']")
    increment = driver.find_element(By.XPATH, "/html//input[@id='input-quantity']")
    buy_now = driver.find_element(By.CSS_SELECTOR, "button#button-cart")
    payment_month.click()
    increment.clear()
    increment.send_keys('4')
    buy_now.click()


@pytest.mark.order(3)
def test_confirm_item():
    confirm = driver.find_element(By.CSS_SELECTOR, '.checkout-btn > .btn.st-outline')
    confirm.click()
    driver.find_element(By.CSS_SELECTOR, '.close.material-icons').click()
    first_name = driver.find_element(By.NAME, 'firstname')
    last_name = driver.find_element(By.NAME, 'lastname')
    address_1 = driver.find_element(By.NAME, 'address_1')
    telephone = driver.find_element(By.NAME, 'telephone')
    email = driver.find_element(By.NAME, 'email')
    city = driver.find_element(By.NAME, 'city')
    zone = driver.find_element(By.NAME, 'zone_id')
    commnet = driver.find_element(By.CSS_SELECTOR, "textarea[name='comment']")
    confirm_order = driver.find_element(By.XPATH, "/html//button[@id='button-confirm']")
    assert first_name.is_displayed() == True and first_name.is_enabled() == True
    first_name.send_keys('Md ')
    assert last_name.is_selected() != True and last_name.is_enabled() == True
    last_name.send_keys('Ketty ')
    assert address_1.is_displayed() == True
    address_1.send_keys('Uttara ')
    assert telephone.is_selected() != True
    telephone.send_keys('01012015139')
    assert email.is_displayed() == True
    email.send_keys('sagor@gmail.com')
    city.send_keys('Mazbari')
    all_zone = Select(zone)
    for all_zones in all_zone.options:
        print(all_zones.text)
        if all_zones.text == 'Rangpur City':
            all_zones.click()
            break
    commnet.send_keys('Hello Startech..')
    confirm_order.click()
