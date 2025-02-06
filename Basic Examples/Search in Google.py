#Import Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

#Open browser
driver = webdriver.Chrome()
driver.get("https://www.google.com")

#Find the text box and type in
elementSearchBox = driver.find_element(By.NAME, 'q')
elementSearchBox.click()
elementSearchBox.send_keys('Selenium')

#Find the Search button and click on it
elementSearchButton = driver.find_element(By.CLASS_NAME, 'gNO89b')
elementSearchButton.click()

driver.quit()