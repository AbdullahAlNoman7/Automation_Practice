from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class DemoLogin:
    def test_setup_login(self):
        global driver
        driver = webdriver.Chrome(executable_path="G:\\SQA\\Automation_practice\\driver\\chrome\\chromedriver.exe")
        # maximum window
        driver.maximize_window()
        driver.implicitly_wait(5)
        # url
        driver.get("https://www.startech.com.bd/")

    def login(self):
        login = driver.find_element(By.LINK_TEXT, 'Login')
        login.click()
        time.sleep(2)
        # user login form
        userName = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        lgnBtn = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/form/button')
        # send data
        userName.send_keys('sagor1751@gmail.com')
        password.send_keys('#123456#')
        lgnBtn.click()
        time.sleep(5)

    # def tearDown(self):
    #     print('successfully done')
    #     driver.close()


dmlgn = DemoLogin()
dmlgn.test_setup_login()
dmlgn.login()


class InfoChange:
    def change_info(self):
        driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/a/span[2]').click()
        time.sleep(3)
        # change address
        change_add = driver.find_element(By.XPATH, '/html/body/div[6]/ul/li[4]/a')
        change_add.click()
        time.sleep(3)
        """
        # Click address
        clk_add_address = driver.find_element(By.CSS_SELECTOR, '.card.add-new')
        clk_add_address.click()
        time.sleep(2)
        
        # scroll the page
        find_address = driver.find_element(By.NAME,'address_1')
        driver.execute_script("arguments[0].scrollIntoView();",find_address)
        
        # add address
        first_name = driver.find_element(By.NAME, 'firstname')
        last_name = driver.find_element(By.NAME, 'lastname')
        add_address1 = driver.find_element(By.NAME, 'address_1')
        add_address2 = driver.find_element(By.NAME, 'address_2')
        city = driver.find_element(By.NAME, 'city')
        element = driver.find_element(By.ID, 'input-zone')
        drp = Select(element)
        first_name.send_keys('Md ')
        last_name.send_keys('hlw')
        add_address1.send_keys('Dhaka Uttara')
        add_address2.send_keys('Badaldi Uttara')
        city.send_keys('Rashahi')
        drp.select_by_index(3)
        time.sleep(2)
        # check radio box
        chk_radio_box = driver.find_element(By.XPATH, '/html/body/div[5]/form/div[7]/label[3]/input').is_selected()
        print(chk_radio_box)
        submit = driver.find_element(By.XPATH,'/html/body/div[5]/form/button')
        submit.click()
        time.sleep(3)
        """
        print(driver.title)
        print(driver.current_url)
        print('Succesful ')

    def delete_address(self):
        # scroll
        driver.execute_script("window.scrollBy(0,300)")
        """
        # edit address
        edit_address = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div[2]/div[2]/a[1]/span')
        edit_address.click()
        """
        # delete address
        delete_address = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div[2]/div[2]/a[2]/span')
        delete_address.click()
        time.sleep(2)


infChange = InfoChange()
infChange.change_info()
infChange.delete_address()

