import selenium.webdriver
from selenium.webdriver.common.by import By
from .locators import Locator

class Final_Page(object):

    def __init__(self, driver):
        self.driver = driver
        self.user_tab = driver.find_element(By.XPATH, Locator.user_tab)

    def getUser_Tab(self):
        return self.user_tab


class Final_Page2(object):

    def __init__(self, driver):
        self.signout = driver.find_element(By.XPATH, Locator.signout)

    def getSignout(self):
        return self.signout