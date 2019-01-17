from selenium import webdriver
import time

driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Selenium Automation")
time.sleep(2)
driver.close()
driver.quit()
print("Test Completed")
