from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options, executable_path =  "../drivers/chromedriver.exe")
driver.get("https://google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Selenium Automation")
driver.close()
driver.quit()
print("Test Completed")