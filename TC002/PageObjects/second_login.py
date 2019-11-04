import selenium.webdriver
from selenium.webdriver.common.by import By
from .locators import Locator

class Second_Login(object):

    def __init__(self, driver):
        self.driver = driver
        self.kontynuuj = driver.find_element(By.ID, Locator.kontynuuj)

    def getKontynuuj(self):
        return self.kontynuuj