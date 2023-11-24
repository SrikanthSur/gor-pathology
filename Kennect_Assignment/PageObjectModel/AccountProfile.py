from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Accountdetail:
    Profileicon = '//button[@aria-controls="menu-appbar"]'
    username = '//*[@id="simple-popover"]/div[3]/div/div[3]'
    logout_buttons = '//button/span[contains(text(),"out")]'


    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)


    def Clickprofile(self):
        self.driver.find_element(By.XPATH, self.Profileicon).click()

    def textprofile(self):
        self.driver.find_element(By.XPATH, '//*[@id="simple-popover"]/div[3]/div').text()

    def ClickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_buttons).click()

