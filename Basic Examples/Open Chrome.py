#Import the Selenium library
from selenium import webdriver

#Creates a driver for Chrome browser, you might need to specify the path of the webdriver, due to my config installation, it is not needed.
driver = webdriver.Chrome()

#Opens google.com , you need to specify the complete url including https
driver.get("https://www.google.com")

#Closes the browser
driver.quit()
