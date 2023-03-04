from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class WebElement:
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="G:\SQA\Automation_practice\driver\chrome\chromedriver.exe")
        # maximum window
        driver.maximize_window()
        driver.implicitly_wait(5)
        # url
        url = driver.get("https://www.startech.com.bd/")
    def actionChanis(self):
        laptop = driver.find_element(By.XPATH,'//*[@id="main-nav"]/div/ul/li[2]/a')
        time.sleep(2)
        all_laptop = driver.find_element(By.XPATH,'//*[@id="main-nav"]/div/ul/li[2]/ul/li[1]/a')
        time.sleep(2)
        hp_laptop = driver.find_element(By.XPATH,'//*[@id="main-nav"]/div/ul/li[2]/ul/li[1]/ul/li[4]/a')
        time.sleep(2)
        acton_chain = ActionChains(driver)
        acton_chain.move_to_element(laptop).move_to_element(all_laptop).move_to_element(hp_laptop).click().perform()
        time.sleep(5)
        # Action chain offset
        elm1 = driver.find_element(By.XPATH,'//*[@id="rang-slider"]/div/div[2]/div')
        elm2 = driver.find_element(By.XPATH,'//*[@id="rang-slider"]/div/div[3]/div')
        action_by_offest = ActionChains(driver)
        action_by_offest.drag_and_drop_by_offset(elm1,50,0).perform()
        action_by_offest.drag_and_drop_by_offset(elm2,-50,0).perform()
        time.sleep(5)
    def test_teardown(self):
        print('Test passed successful')
        time.sleep(5)
        driver.close()


Web = WebElement()
Web.test_setup()
Web.actionChanis()
Web.test_teardown()
