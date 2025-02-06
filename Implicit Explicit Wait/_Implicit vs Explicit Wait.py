#---------------------- Here an example where implicit wait fails and explicit wait is the solution
#---------------------- some elements are loaded until random time has elapsed
#---------------------- this random time happens because internet speed, computer power, etc
#---------------------- Explicit wait will wait until the element is enabled, clickable, etc

#----------------------- 2 additional libraries should be imported : WebDriverWait and Expected Conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
#----------------------  common libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Creates the driver and opens the webpage
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# Set the timeout for the current implicit wait and the creates the driver for explicit wait and its timeout
driver.implicitly_wait(10)
driver_wait = WebDriverWait(driver,10)

# click the button to start loading a text box , time to load will vary
button = driver.find_element(By.CSS_SELECTOR,'#input-example > button')
button.click()

#------- using Implicit Wait will fail !
#textBox = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]') # IMPLICIT WAIT
textBox = driver_wait.until(expected_conditions.element_to_be_clickable( (By.CSS_SELECTOR, '#input-example > input[type=text]') ) ) #EXPLICIT WAIT

#----- If correct wait is used, the text is typed into the textbox and test will pass, otherwise it will fail
textBox.send_keys('Correct Wait')

driver.quit()