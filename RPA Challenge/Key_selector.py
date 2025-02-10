from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rpachallenge.com/")

# Finds the element which is sibling to the final target element
# This is done this way because the name of the target changes every time and only this element is constant
# XPATH is used because the CSS selector can not find texts
label = driver.find_element(By.XPATH, "//label[text()='Role in Company']")

# finds the sibling which is the final target
input_element = label.find_element(By.XPATH, "./following-sibling::input")

# To ensure target has been properly selected, writes down a sample
input_element.send_keys("QA Manager")

driver.quit()