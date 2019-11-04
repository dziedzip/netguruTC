import selenium.webdriver
from selenium.webdriver.common.by import By
from .locators import Locator

class Pass_Page(object):

    def __init__(self, driver):
        self.driver = driver
        self.password = driver.find_element(By.ID, Locator.password)
        self.kontynuuj2 = driver.find_element(By.ID, Locator.kontynuuj2)


    def getPass_Field(self):
        return self.password


    def getKontynuuj2(self):
        return self.kontynuuj2