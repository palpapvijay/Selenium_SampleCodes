from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options, executable_path =  "../drivers/chromedriver.exe")
driver.get("https://google.com")
print(driver.title)
driver.close()
driver.quit()
print("Test Completed")