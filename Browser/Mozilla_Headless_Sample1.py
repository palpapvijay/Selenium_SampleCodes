from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("-headless")

path = "../drivers/geckodriver.exe"
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
driver = webdriver.Firefox(capabilities=cap, executable_path=path, options=firefox_options)
driver.set_page_load_timeout(10)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Selenium Automation")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.close()
driver.quit()
print("Test Completed")
