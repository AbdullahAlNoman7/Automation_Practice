import pytest
import unittest
import time
import allure
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.yield_fixture()
def browser_setup():
    global driver
    global wait
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get('https://automationexercise.com/')
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)

    yield
    print(driver.title)


@pytest.mark.skip("Already created..")
@pytest.mark.order(1)
def test_click_singUp(browser_setup):
    # click the login/SingUp
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    # locate username and email input field
    userName_field = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
    email_field = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
    singUp = driver.find_element(By.XPATH, "//button[normalize-space()='Signup']")

    # check statement
    expected_title = driver.title
    actual_title_false = "Automation Exercise"
    actual_title = "Automation Exercise - Signup / Login"

    # check condition
    if expected_title == actual_title:
        userName_field.send_keys("sagor")
    if email_field.is_displayed() and email_field.is_enabled():
        email_field.send_keys("sagor@gmail.com")
    singUp.send_keys(Keys.RETURN)


@pytest.mark.skip("Already created..")
@pytest.mark.order(2)
def test_register_info():
    # locate account information
    time.sleep(3)
    title_filed_mr = driver.find_element(By.ID, "uniform-id_gender1")
    password_field = driver.find_element(By.XPATH, "/html//input[@id='password']")

    # DOB
    days_field = driver.find_element(By.NAME, "days")
    month_field = driver.find_element(By.ID, "months")
    years_field = driver.find_element(By.ID, "years")

    # Address Information locate
    firstName_field = driver.find_element(By.ID, "first_name")
    lastName_field = driver.find_element(By.ID, "last_name")
    company_field = driver.find_element(By.ID, "company")
    address1_field = driver.find_element(By.NAME, "address1")
    address2_field = driver.find_element(By.NAME, "address2")
    country_field = driver.find_element(By.ID, "country")
    state_field = driver.find_element(By.ID, "state")
    city_field = driver.find_element(By.ID, "city")
    zipcode_field = driver.find_element(By.ID, "zipcode")
    mobileNumber_field = driver.find_element(By.ID, "mobile_number")
    clcik_create_account = driver.find_element(By.XPATH, "//button[normalize-space()='Create Account']")

    # condition check
    expected_title = driver.find_element(By.XPATH, "//b[normalize-space()='Enter Account Information']").text
    actual_title = "Enter Account Information"

    # enter all data field and check condition
    if title_filed_mr.is_displayed() and title_filed_mr.is_enabled():
        title_filed_mr.click()
    time.sleep(2)
    password_field.send_keys("123456")
    # DOB
    days_select = Select(days_field)
    for all_days in days_select.options:
        # print("Days ...", all_days.text)
        if all_days.text == "7":
            all_days.click()
            break
    time.sleep(2)
    months_select = Select(month_field)
    for all_months in months_select.options:
        # print("Months ...", all_months.text)
        if all_months.text == "April":
            all_months.click()
            break
    time.sleep(2)
    years_select = Select(years_field)
    for all_years in years_select.options:
        # print("Months ...", all_years.text)
        if all_years.text == "2020":
            all_years.click()
            break
    time.sleep(2)

    # address information entery
    if firstName_field.is_displayed():
        try:
            firstName_field.send_keys("Md")
        except:
            print("Logical error firstName...")

    try:
        lastName_field.send_keys("Sagor")
    except:
        print("Logical error lastName...")

    if not company_field.is_selected():
        company_field.send_keys("S.J")
    else:
        print("Logical error company...")

    address1_field.clear()
    address1_field.send_keys("Dhaka")
    address2_field.clear()
    address2_field.send_keys("Uttara")

    country_select = Select(country_field)
    for all_country in country_select.options:
        # print("Days ...", all_days.text)
        if all_country.text == "New Zealand":
            all_country.click()
            break

    state_field.send_keys("Dhaka")
    city_field.send_keys("city")
    zipcode_field.send_keys("120")
    mobileNumber_field.send_keys("12357894")
    time.sleep(5)
    clcik_create_account.click()


@pytest.mark.order(3)
def test_login(browser_setup):
    # click the login/SingUp
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    email_field = driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    click_login = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")

    # check statement
    expected_title = driver.title
    actual_title = "Automation Exercise - Signup / Login"
    assert email_field.is_enabled() and email_field.is_displayed()
    email_field.send_keys("sagor@gmail.com")

    if expected_title == actual_title:
        try:
            password_field.send_keys("123456")
        except:
            print("Logical error password...")
    click_login.send_keys(Keys.RETURN)


@pytest.mark.order(4)
def test_add_to_cart():
    time.sleep(5)
    click_product = driver.find_element(By.CSS_SELECTOR, "[href='\/products']")
    click_product.click()
    # filter
    # click_men = driver.find_element(By.LINK_TEXT, "MEN")
    # click_men.click()
    # t_shart = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "TSHIRTS")))
    # t_shart.click()
    scroll = driver.find_element(By.CSS_SELECTOR, "[href='\/product_details\/1']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll)
    time.sleep(3)
    blue_top = driver.find_element(By.CSS_SELECTOR, "[href='\/product_details\/1']")
    blue_top.click()
    time.sleep(2)
    quantity = wait.until(EC.presence_of_element_located((By.ID, "quantity")))
    quantity.send_keys("2")
    add_to_cart = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.cart")
    add_to_cart.click()
    time.sleep(2)

    actual_title = driver.title
    if actual_title == "Automation Exercise - Product Details":
        print("Success...")
        assert True
    else:
        allure.attach(driver.get_screenshot_as_png(),name="add to cart failed",attachment_type=AttachmentType.PNG)
        assert False
