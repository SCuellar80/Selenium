from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.google.com")

# This works in headless mode also
driver.save_screenshot("My Screenshot.png")   #takes screenshot and save it in current path of this file

driver.quit()
