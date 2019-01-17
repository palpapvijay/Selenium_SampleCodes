from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("../drivers/chromedriver.exe")
#driver.implicitly_wait(10)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Selenium Automation")

wait = WebDriverWait(driver, 10)
try:
    element = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
    print("Element Clickable")
except:
    print("Element Non Clickable")

driver.close()
driver.quit()
print("Test Completed")
