import unittest
import HtmlTestRunner
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= "../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search1(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Setup")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Automation Setup - Google Search")

    def test_search2(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Vijay")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Vijay1 - Google Search")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/vijayago/PycharmProjects/Sample_Project/HTML Reports/Reports'))
