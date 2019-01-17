from selenium import webdriver
import HtmlTestRunner
import unittest


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Selenium Automation")
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Sample_Project/Sample_Project1/Reports'))
