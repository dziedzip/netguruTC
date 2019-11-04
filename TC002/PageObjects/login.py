import selenium.webdriver
from selenium.webdriver.common.by import By
from .locators import Locator

class Login_Page(object):

    def __init__(self, driver):
        self.driver = driver
        self.email_field = driver.find_element(By.ID, Locator.email_field)
        self.zalogujatl = driver.find_element(By.ID, Locator.zalogujatl)


    def getEmail_field(self):
        return self.email_field


    def getZalogujAtl(self):
        return self.zalogujatl