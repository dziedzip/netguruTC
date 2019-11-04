import unittest
import selenium.webdriver
import time
import HtmlTestRunner
import logging
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from PageObjects.main import Main_Page
from PageObjects.login import Login_Page
from PageObjects.second_login import Second_Login
from PageObjects.password_page import Pass_Page
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


    def testCase002_Step1(self):
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

    def testCase002_Step2(self):
        print("Setp2")
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

    def testCase002_Step3(self):
        print("Setp3")
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

    def testCase002_Step4(self):
        print("Setp4")
        password_page = Pass_Page(self.driver)
        pass_field = password_page.getPass_Field()
        button2 = password_page.getKontynuuj2()
        try:
            pass_field.send_keys(cred[5])
            print("Pass: Password submitted!")
            logging.info("Pass: Password submitted!")
            self.driver.execute_script("arguments[0].click();", button2)
            time.sleep(3)
            time.sleep(3)
        except:
            print("     Fail: Button 'Zaloguj' not displayed")
            logging.info("     Fail: Button 'Zaloguj' not displayed")
            now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
            self.driver.save_screenshot(evidence_path + now + ' - step4         FAIL.png')
            raise Exception("     Fail: Button does not work")


    def testCase002_Step5(self):
        print("Setp5")
        driver = self.driver
        try:
            title = self.driver.title
            self.assertEqual("Tablice | Trello", title)
            now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
            self.driver.save_screenshot(evidence_path + now + ' PASS.png')
            print("Pass: User logged in!")
            logging.info("Pass: User logged in!")
        except:
            print("     Fail: Login Failed")
            logging.info("     Fail: Login Failed")
            now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
            self.driver.save_screenshot(evidence_path + now + ' - step5         FAIL.png')
            raise AssertionError("      Fail: Login Failed")

    def testCase002_Step6(self):
        driver = self.driver
        print("Setp6")
        final_page = Final_Page(self.driver)
        button5 = final_page.getUser_Tab()    
        try:
            self.driver.execute_script("arguments[0].click();", button5)
            final_page2 = Final_Page2(self.driver)
            button6 = final_page2.getSignout()
            self.driver.execute_script("arguments[0].click();", button6)
            print("Pass: Button 'Wyloguj' works!")
            logging.info("Pass: Button 'Wyloguj' works!")
            time.sleep(3)
        except:
            print("     Fail: Button 'Wyloguj' not working")
            logging.info("     Fail: Button 'Wyloguj' not working")
            now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
            self.driver.save_screenshot(evidence_path + now + ' - step6         FAIL.png')
            raise Exception("     Fail: Button does not work")

    def testCase002_Step7(self):
        driver = self.driver
        print("Setp7")
        try:
            title = self.driver.title
            self.assertEqual("Wylogowany z Trello", title)
            print("Pass: User logged out!")
            logging.info("Pass: User logged out!")
            now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
            self.driver.save_screenshot(evidence_path + now + ' PASS.png')
        except:
            print("     Fail: Log out Failed")
            logging.info("     Fail: Log out Failed")
            now = datetime.today().strftime('%Y-%m-%d,  %H.%M.%S')
            self.driver.save_screenshot(evidence_path + now + ' - step7         FAIL.png')
            raise AssertionError("      Fail: Log out Failed")



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output = 'Report'))