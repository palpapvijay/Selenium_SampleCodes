from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



path = "../drivers/IEDriverServer.exe"
driver = webdriver.Ie(executable_path=path)
driver.set_page_load_timeout(10)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Selenium Automation")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.close()
driver.quit()
print("Test Completed")
