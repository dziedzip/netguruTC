from functions import XLUtils
import unittest
import selenium.webdriver
import time
import HtmlTestRunner
import logging
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from PageObjects.main import Main_Page
from PageObjects.login import Login_Page, Login_PageError
from PageObjects.second_login import Second_Login
from PageObjects.password_page import Pass_Page, Pass_PageMessage
from PageObjects.final_page import Final_Page, Final_Page2

# email addres and password imported from the email.txt file
source = open ('email.txt', 'r')
cred = source.read().split()

# Evidence path (screenshots)
evidence_path = 'Evidence/'

# log file in Error mode. To save space choose different logging option. 
# Keep in mind, that DEBUG mode dumps the email password to the log!
log_file = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S') + ".log"
logging.basicConfig(filename="logs/" + log_file,
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.INFO)

# Test data feeder
data_path = "testdata/data.xlsx"
rows = XLUtils.getRowCount(data_path, 'Arkusz1')

class Trello(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("========== testCase02 STARTS ==========")
        logging.info("========== testCase02 STARTS ==========")
        cls.driver = selenium.webdriver.Chrome()
        cls.driver.get("https://trello.com/")
        cls.driver.maximize_window()
        now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
        cls.driver.save_screenshot(evidence_path + now + ' PASS.png')
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("========== testCase02 finished ==========")
        logging.info("========== testCase02 finished ==========")


    def testCase004_Step1(self):
        main_page = Main_Page(self.driver)
        button = main_page.getZaloguj()
        print("Step1")
        try:
            # button = driver.find_element(By.XPATH, '/html/body/header/nav/div[2]/a[1]')
            self.driver.execute_script("arguments[0].click();", button)
            print("Pass: Button 'Zaloguj' was clicked")
            logging.info("Pass: Button 'Zaloguj' was clicked")
            time.sleep(3)
        except:
            print("     Fail: Button 'Zaloguj' cannot be clicked")
            logging.info("     Fail: Button 'Zaloguj' cannot be clicked")
            now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
            self.driver.save_screenshot(evidence_path + now + ' - step1         FAIL.png')
            raise Exception ("     Fail: Button 'Zaloguj' cannot be clicked")

# First negative
    def testCase004_Step2(self):
        print("Setp2")
        login_page = Login_Page(self.driver)
        field = login_page.getEmail_field()
        button = login_page.getZalogujAtl()
        # passing empty string as imput
        self.driver.execute_script("arguments[0].click();", button)
        try:
            for r in range(2, rows + 1):
                email = XLUtils.readData(data_path, 'Arkusz1', r, 1)
                field.send_keys(email)
                self.driver.execute_script("arguments[0].click();", button)
                time.sleep(1)
                print("Pass: Button 'Zaloguj' works!")
                try:
                    error_message = Login_PageError(self.driver)
                    error_mess = error_message.getError_Field()
                    error_mess.is_displayed() == True
                    print("Pass: Error message present!\n")
                    logging.info("Pass: Error message present!\n")
                    now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
                    self.driver.save_screenshot(evidence_path + now + ' - step2         PASS.png')
                    field.clear()
                except:
                    error_message = Login_PageError(self.driver)
                    error_mess = error_message.getError_Field()
                    print("      FAIL: Error message NOT present!\n")
                    logging.info("      FAIL: Error message NOT present!")
                    now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
                    self.driver.save_screenshot(evidence_path + now + ' - step2         FAIL.png')
                    field.clear()
        except:
            print("     Fail: Button 'Zaloguj' not displayed")
            logging.info("     Fail: Button 'Zaloguj' not displayed")
            now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
            self.driver.save_screenshot(evidence_path + now + ' - step2         FAIL.png')
            raise Exception("     Fail: Button does not work")


# Positive
    def testCase004_Step3(self):
        print("Setp3")
        login_page = Login_Page(self.driver)
        field = login_page.getEmail_field()
        button = login_page.getZalogujAtl()
        try:
            field.send_keys(cred[2])
            time.sleep(1)
            print("Pass: Email accepted!")
            logging.info("Pass: Email accepted!")
            self.driver.execute_script("arguments[0].click();", button)
            print("Pass: Button 'Zaloguj' works!")
            logging.info("Pass: Button 'Zaloguj' works!")
        except:
            print("     Fail: Button 'Zaloguj' not displayed")
            logging.info("     Fail: Button 'Zaloguj' not displayed")
            now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
            self.driver.save_screenshot(evidence_path + now + ' - step2         FAIL.png')
            raise Exception("     Fail: Button does not work")


    def testCase004_Step4(self):
        print("Setp4")
        second_login = Second_Login(self.driver)
        button = second_login.getKontynuuj()
        try:
            self.driver.execute_script("arguments[0].click();", button)
            print("Pass: Button 'Kontynuuj' works again!")
            logging.info("Pass: Button 'Kontynuuj' works again!")
            time.sleep(1)
        except:
            print("     Fail: Button 'Zaloguj' not displayed")
            logging.info("     Fail: Button 'Zaloguj' not displayed")
            now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
            self.driver.save_screenshot(evidence_path + now + ' - step3         FAIL.png')
            raise Exception("     Fail: Button does not work")

    def testCase004_Step5(self):
        print("Setp5")
        password_page = Pass_Page(self.driver)
        pass_field = password_page.getPass_Field()
        button2 = password_page.getKontynuuj2()
        # passing empty string as imput
        self.driver.execute_script("arguments[0].click();", button2)
        try:
            for r in range(2, 13):
                email = XLUtils.readData(data_path, 'Arkusz1', r, 2)
                pass_field.send_keys(email)
                self.driver.execute_script("arguments[0].click();", button2)
                time.sleep(1)
                print("Pass: Button 'Zaloguj' works!")
                pass_field.clear()
                try:
                    error_message = Pass_PageMessage(self.driver)
                    error_mess = error_message.getPass_FieldMessage()
                    error_mess.is_displayed() == True
                    print("Pass: Error message present!\n")
                    logging.info("Pass: Error message present!\n")
                    now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
                    self.driver.save_screenshot(evidence_path + now + ' - step2         PASS.png')
                except:
                    print("      FAIL: Error message NOT present!")
                    raise Exception("     FAIL: Error message NOT present!")
                    logging.info("      FAIL: Error message NOT present!")
                    now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
                    self.driver.save_screenshot(evidence_path + now + ' - step2         FAIL.png')
        except:
            print("     Fail: Button 'Zaloguj' not displayed")
            logging.info("     Fail: Button 'Zaloguj' not displayed")
            now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
            self.driver.save_screenshot(evidence_path + now + ' - step2         FAIL.png')
            raise Exception("     Fail: Button does not work")

# Captcha

    def testCase004_Stepx6(self):
        driver = self.driver
        print("Setp6")
        password_page = Pass_Page(self.driver)
        button2 = password_page.getKontynuuj2()
        try:
            button2.is_enabled() == False
            print("Pass: Captcha works!")
            logging.info("Pass: Error message present!")
            now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
            self.driver.save_screenshot(evidence_path + now + ' - step2         PASS.png')
        except:
            print("     Fail: No Captcha!!!")
            logging.info("     Fail: Button 'Zaloguj' not displayed")
            now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
            self.driver.save_screenshot(evidence_path + now + ' - step2         FAIL.png')
            raise Exception("     Fail: No Captcha!!!")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output = 'Report'))
