from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Loginpage:
    email = '//input[@name="email"]'
    password = '//input[@name="password"]'
    Login_button = '//span[text()="Login"]'
    Recovery_Passwoard = '//u[text()="Recover or set password"]'
    login_with_google = '//div[text()="Login in with Google"]'


    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def EnterEmail(self):
        self.driver.find_element(By.XPATH, self.email).click()
        self.driver.find_element(By.XPATH, self.email).send_keys("test@kennect.io")
    def EnterPassword(self):
        self.driver.find_element(By.XPATH, self.password).click()
        self.driver.find_element(By.XPATH, self.password).send_keys("Qwerty@1234")

    def ClickLoginbutton(self):
        self.driver.find_element(By.XPATH, self.Login_button).click()

    def clickRecoverbutton(self):
        self.driver.find_element(By.XPATH, self.Recovery_Passwoard).click()


class invalidlogindetail:
    email = '//input[@name="email"]'
    password = '//input[@name="password"]'
    Login_button = '//span[text()="Login"]'
    Recovery_Passwoard = '//u[text()="Recover or set password"]'
    login_with_google = '//div[text()="Login in with Google"]'

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def EnterEmail(self):
        self.driver.find_element(By.XPATH, self.email).click()
        self.driver.find_element(By.XPATH, self.email).send_keys("Qwerty@1234")

    def EnterPassword(self):
        self.driver.find_element(By.XPATH, self.password).click()
        self.driver.find_element(By.XPATH, self.password).send_keys("Qwerty@1234")

    def ClickLoginbutton(self):
        self.driver.find_element(By.XPATH, self.Login_button).click()

