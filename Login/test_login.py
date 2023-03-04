import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select

import time
import unittest


class NopCommerceLogin(unittest.TestCase):
    global driver

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.get("https://demo.nopcommerce.com/")
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_login(self):
        click_login = self.driver.find_element(By.LINK_TEXT, "Log in")
        # check condition
        expected_title = "nopCommerce demo store"
        self.assertEqual(expected_title, self.driver.title)
        click_login.click()

        # select located element
        email_field = self.driver.find_element(By.ID, "Email")
        password_filed = self.driver.find_element(By.ID, "Password")
        login = self.driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")

        # input data
        self.assertEqual(email_field.is_enabled(), email_field.is_displayed())
        email_field.send_keys("hello1@gmail.com")
        self.assertTrue(password_filed.is_displayed(), password_filed.is_enabled())
        try:
            password_filed.send_keys("1234567")
        except:
            print("error....")
        login.click()

        expected_error = "Login was unsuccessful. Please correct the errors and try again."
        if expected_error == True:
            try:
                self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\login1.png")
            except:
                print("No error....")


if __name__ == "__main__":
    unittest.main()
