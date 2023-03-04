import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BimanTicket:

    def demo_ticket(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://www.gozayaan.com/')
        # one way select
        driver.find_element(By.CSS_SELECTOR, '.flight-type-wrapper .radio:nth-of-type(1)').click()
        # confirm ticket
        click_input_from = driver.find_element(By.CSS_SELECTOR, '.box.from.location > .value')
        click_input_from.click()
        input_box_from = driver.find_elements(By.XPATH, "/html//div[@id='searchbar']//div["
                                                        "@class='airport-suggestion']/div[@class='airport-list']//div["
                                                        "1]/div")
        print(len(input_box_from))
        for result in input_box_from:
            if result.text == "New York, United States":
                result.click()
                break
        click_input_to = driver.find_element(By.CSS_SELECTOR, '.box.has-swapper.location.to > .value')
        click_input_to.click()
        input_box_to = driver.find_elements(By.XPATH, "/html//div[@id='searchbar']//div["
                                                      "@class='airport-suggestion']//div[1]/div")
        print(len(input_box_to))
        for results in input_box_to:
            if results.text == "Dhaka, Bangladesh":
                results.click()
                break
        journy_date = driver.find_element(By.CSS_SELECTOR, '.flight-search div:nth-of-type(3) .value')
        journy_date.click()
        selct_date = driver.find_element(By.CSS_SELECTOR, '.calendar.left > .month > span:nth-of-type(16)')
        selct_date.click()
        return_date = driver.find_element(By.CSS_SELECTOR, '.box.date.return > .label')
        return_date.click()
        select_return_date = driver.find_element(By.CSS_SELECTOR, '.calendar.right > .month > span:nth-of-type(9)')
        select_return_date.click()
        travel_cls = driver.find_element(By.CSS_SELECTOR, '.box.traveler')
        travel_cls.click()
        # adult
        driver.find_element(By.CSS_SELECTOR, ".adults .input-container .btn-link:nth-child(3)").click()
        # children
        driver.find_element(By.CSS_SELECTOR, ".children > .input-container > button:nth-of-type(2)").click()
        children_age = driver.find_element(By.CSS_SELECTOR, '.brand-input.custom-select.small')
        sel = Select(children_age)
        sel.select_by_value('2')
        # infant
        driver.find_element(By.CSS_SELECTOR, ".infants .input-container .btn-link:nth-child(3)").click()
        # business cls
        driver.find_element(By.CSS_SELECTOR, '.radio-container .brand-radio:nth-of-type(2) .text').click()
        driver.find_element(By.CSS_SELECTOR, '.btn.btn-secondary.picker-mb-btn').click()
        # search
        driver.find_element(By.XPATH, "//div[@id='searchbar']//button[@type='button']").click()
        # select ticekt
        wait = WebDriverWait(driver, 80)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@id='flight-list']/div[@class='container']/div[@class='row']/div["
                       "@class='col-lg-9']/div[2]/div[@class='flight-card']//button["
                       "@type='button']"))).click()
        # send user info
        scroll = driver.find_element(By.CSS_SELECTOR,".collapse.show > div > div:nth-of-type(1) > .col-12.mb-1 > "
                                                     ".font-weight-bolder.text-primary")
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        # driver.find_element(By.XPATH,'//*[@id="__BVID__521"]/div/span/div/div[1]/label/div/span').click()
        # mr.click
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/span/div[1]/div/span/div["
                                      "2]/div/div[1]/div[2]/fieldset/div/span/div/div[1]/label/div").click()
        first_name = driver.find_element(By.ID, "first-name-0")
        last_name = driver.find_element(By.ID, "last-name-0")
        first_name.send_keys("Mr")
        last_name.send_keys("Sagor")
        bob = driver.find_element(By.ID, "birth-date-0")
        bob.click()
        driver.find_element(By.CSS_SELECTOR, "[for='birth-date-0'] div .weekend:nth-of-type(20)").click()
        serach = driver.find_element(By.CSS_SELECTOR, "[class] span:nth-child(6) > div:nth-of-type(1) .vs__search")
        serach.click()
        serach.clear()
        serach.send_keys('China')
        driver.find_element(By.ID, "email-0").send_keys('sagor@gmail.com')  # email
        driver.find_element(By.ID, "phone-number-0").send_keys('12456217569')  # phone number
        driver.find_element(By.ID, "passport-number-0").send_keys('21447982462')  # passport number
        expire_date = driver.find_element(By.ID, "passport-expiry-0")
        expire_date.click()
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/span/div[1]/div/span/div["
                                      "2]/div/div[3]/div[3]/fieldset/div/span/div/div/div[2]/div/span[27]").click()
        # driver.find_element(By.ID, "bookButton").click()  # continue


tickt_obj = BimanTicket()
tickt_obj.demo_ticket()

