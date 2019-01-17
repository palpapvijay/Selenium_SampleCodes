from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POM.Pages.loginpage import LoginPage
from POM.Pages.homepage import Homepage
import HtmlTestRunner

class Logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = Homepage(driver)
        homepage.click_welcome()
        homepage.click_logout()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/vijayago/PycharmProjects/Sample_Project/POM/Reports'))

