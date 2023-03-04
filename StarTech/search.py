from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import Login

class SearchIteam:
    def test_setup_login(self):
        global driver
        driver = webdriver.Chrome(executable_path="G:\\SQA\\Automation_practice\\driver\\chrome\\chromedriver.exe")
        # maximum window
        driver.maximize_window()
        driver.implicitly_wait(5)
        # url
        driver.get("https://www.startech.com.bd/")

    def search(self):
        #serach item
        search_item = driver.find_element(By.NAME,'search')
        search_item.send_keys('Mouse')
        srcbtn = driver.find_element(By.XPATH,'//*[@id="search"]/button')
        srcbtn.click()
        time.sleep(5)
        # scroll page and clcik
        scroll = driver.find_element(By.LINK_TEXT,'Logitech M190 Wireless Mouse')
        # driver.execute_script("arguments[0].scrollIntoView();", scroll)
        scroll.click()
        time.sleep(2)
        """
        # close popup
        # driver.find_element(By.XPATH,'/html/body/div[7]/div/span').click()
        # click item
        emi = driver.find_element(By.CLASS_NAME,'p-wrap active')
        emi.click()
        print(emi.is_selected())
        time.sleep(2)
        """
        item_number = driver.find_element(By.XPATH,'//*[@id="product"]/div/div[5]/label/span[3]/i')
        item_number.click()
        time.sleep(3)
        buy_btn = driver.find_element(By.ID,'button-cart')
        buy_btn.click()
        time.sleep(5)
        # close the popup


searchobj = SearchIteam()
searchobj.test_setup_login()
searchobj.search()
