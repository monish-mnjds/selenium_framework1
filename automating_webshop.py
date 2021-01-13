from Library.Config import *
driver = webdriver.Chrome(driverpath)
driver.implicitly_wait(3)

class AutomatingWebshop:
    def launch_url(self):
        driver.get(URL)
        driver.maximize_window()

    def click_reg(self):
        driver.find_element_by_xpath("//a[@class='ico-register']").click()

    def click_radio(self):
        driver.find_element_by_xpath("//input[@id='gender-male']").click()

    def enter_fname(self):
        driver.find_element_by_id("FirstName").send_keys("Virat")

    def enter_lname(self):
        driver.find_element_by_id("LastName").send_keys("Kohli")

    def enter_email(self):
        driver.find_element_by_xpath("//input[@id='Email']").send_keys("viratkohli18@gmail.com")

    def enter_password(self):
        driver.find_element_by_xpath("//input[@id='Password']").send_keys("viratvirat18")

    def confirm_password(self):
        driver.find_element_by_xpath("//input[@id='ConfirmPassword']").send_keys("viratvirat18")

    def click_register(self):
        driver.find_element_by_xpath("//input[@id='register-button']").click()