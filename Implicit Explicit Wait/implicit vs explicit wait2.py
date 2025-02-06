from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://www.bing.com/")

elementSearchBox = driver.find_element(By.NAME, "q")
elementSearchBox.click()
elementSearchBox.send_keys("Python with Selenium")

#------ Use this way if you want to reduce to one line finding the elements with explicit waits
elementSearchButton = WebDriverWait(driver,10).until( expected_conditions.element_to_be_clickable( (By.CSS_SELECTOR, "ul[role='listbox'] li[query='python with selenium']") ) )
elementSearchButton.click()

driver.quit()