from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://rpachallenge.com/")

input_element = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelAddress']")

# To ensure target has been properly selected, writes down a sample
input_element.send_keys("My Address")

driver.quit()