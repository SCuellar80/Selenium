from selenium import webdriver

driver = webdriver.Firefox() #for Firefox
driver.get("https://www.google.com")
driver.quit()
