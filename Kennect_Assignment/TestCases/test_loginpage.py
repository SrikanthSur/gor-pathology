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

    def test_loginPageURL(self, setup):
        self.logger.info(" *********** Verifing loginPageURL *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        page_url = self.driver.current_url
        if 'gor-pathology' in page_url:
            assert True
            self.driver.close()
            self.logger.info(" *********** loginPageURL TestCase Passed *********** ")
        else:
            self.driver.save_screenshot("D:\pythonProject\Screenshots\\" + "test_loginPageURL.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_loginPageURL.png",attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.logger.error(" *********** loginPageURL TestCase Failed *********** ")
            assert False

    # @pytest.mark.sanity
    # @pytest.mark.regression
    # @allure.severity(allure.severity_level.CRITICAL)
    def test_loginPageTitle(self, setup):
        self.logger.info(" *********** Verifing loginPageTitle *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        page_title = self.driver.title
        if 'GOR Pathology' in page_title:
            assert True
            self.driver.close()
            self.logger.info(" *********** loginPageTitle TestCase Passed *********** ")
        else:
            self.driver.save_screenshot("D:\pythonProject\Screenshots\\" + "test_loginPageTitle.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_loginPageTITEL.png",attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.logger.error(" *********** loginPageTitle TestCase Failed *********** ")
            assert False
    def test_login_with_valid_value(self,setup):
        self.logger.info(" *********** Verifing login using valid credentials *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP = Loginpage(self.driver)
        self.LP.EnterEmail()
        self.LP.EnterPassword()
        self.LP.ClickLoginbutton()
        sleep(5)
        self.AD = Accountdetail(self.driver)
        self.AD.Clickprofile()
        username = self.driver.find_element(By.XPATH,'//*[@id="simple-popover"]/div[3]/div').text
        # page_url = self.driver.current_url
        if "test@kennect.io" in username:
            assert True
            self.driver.close()
            self.logger.info(" *********** login using valid credentials TestCase Passed *********** ")
        else:
            self.driver.save_screenshot("D:\pythonProject\Screenshots\\" + "test_loginPageTitle.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_loginPageTITEL.png",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.logger.error(" *********** login using valid credentials TestCase Failed *********** ")
            assert False

    def test_login_with_invalid_value(self,setup):
        self.logger.info(" *********** Verifing login using invalid credentials *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP =invalidlogindetail(self.driver)
        self.LP.EnterEmail()
        self.LP.EnterPassword()
        self.LP.ClickLoginbutton()
        sleep(2)
        Allertmassage = self.driver.find_element(By.XPATH,'//div[@class="MuiAlert-message"]').text

        if "There is no user record corresponding to this identifier. The user may have been deleted." in Allertmassage:
            assert True
            self.driver.close()
            self.logger.info(" *********** login using invalid credentials TestCase Passed *********** ")
        else:
            self.driver.save_screenshot("D:\pythonProject\Screenshots\\" + "test_loginPageTitle.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_loginPageTITEL.png",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.logger.error(" *********** login using invalid credentials TestCase Failed *********** ")
            assert False
    def test_Recoverpasswordlink(self,setup):
        self.logger.info(" *********** Verifing Recover password link *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP = Loginpage(self.driver)
        self.LP.clickRecoverbutton()
        sleep(1)
        current_page = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div').text
        # page_url = self.driver.current_url
        if "Recover" in current_page:
            assert True
            self.driver.close()
            self.logger.info(" *********** Recover password link TestCase Passed *********** ")
        else:
            self.driver.save_screenshot("D:\pythonProject\Screenshots\\" + "test_loginPageTitle.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_loginPageTITEL.png",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.logger.error(" *********** Recover password link TestCase Failed *********** ")
            assert False
