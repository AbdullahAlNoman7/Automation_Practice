from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class BimanTicket:
    def ticket_demo(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://www.biman-airlines.com/')
        wait = WebDriverWait(driver, 10)
        # close_add.click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".close [aria-hidden]"))).click()
        # flying from
        flying_from = driver.find_element(By.ID,"select2-departure2-container")
        flying_from.click()
        type_destination = driver.find_element(By.CSS_SELECTOR,'.select2-search--dropdown [type]')
        all_route = driver.find_elements(By.XPATH,"//body[@class='fixed-nav']//span[@class='select2-dropdown select2-dropdown--below']/span[@class='select2-results']//ul//li")
        for allRoutes in all_route:
            print('the route is ..', allRoutes.text)


ticket_obj = BimanTicket()
ticket_obj.ticket_demo()
