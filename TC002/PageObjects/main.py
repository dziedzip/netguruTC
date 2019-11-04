import selenium.webdriver
from selenium.webdriver.common.by import By
from .locators import Locator

class Main_Page(object):

    def __init__(self, driver):
        self.driver = driver
        self.zaloguj = driver.find_element(By.XPATH, Locator.zaloguj)

    def getZaloguj(self):
        return self.zaloguj