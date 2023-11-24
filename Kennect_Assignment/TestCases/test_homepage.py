import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
import allure
from PageObjectModel.AccountProfile import Accountdetail
from PageObjectModel.LoginPage import Loginpage, invalidlogindetail
from Utilities.customLogger import logGen
from Utilities.readProperties import readConfig
from time import sleep

class Test_LoginPage:
    # baseURL= 'https://gor-pathology.web.app/'
    baseURL = readConfig.getApplicationURL()
    logger = logGen.logGen()

    def test_Logout(self, setup):
        self.logger.info(" *********** Verifing Logout button *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP = Loginpage(self.driver)
        self.LP.EnterEmail()
        self.LP.EnterPassword()
        self.LP.ClickLoginbutton()
        sleep(5)
        self.AD = Accountdetail(self.driver)
        self.AD.Clickprofile()
        self.driver.find_element(By.XPATH,'//button/span[contains(text(),"out")]').click()
        sleep(3)
        page_url = self.driver.current_url

        if 'gor-pathology' in page_url:
            assert True
            self.driver.close()
            self.logger.info(" *********** Logout TestCase Passed *********** ")
        else:
            self.driver.save_screenshot("D:\pythonProject\Screenshots\\" + "test_loginPageURL.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_loginPageURL.png",attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.logger.error(" *********** logout TestCase Failed *********** ")
            assert False
