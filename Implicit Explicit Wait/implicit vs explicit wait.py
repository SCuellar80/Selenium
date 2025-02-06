#---------------------- Here an example where implicit wait fails and explicit wait is the solution


#----------------------- 2 additional libraries should be imported : WebDriverWait and Expected Conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
#----------------------  common libraries
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

#1 difference: implicit is the timeout for all elements and explicit is for certain elements.
#2 difference: explicit wait needs two additional sub-libraries (WebDriverWait and expected_conditions)
#3 difference: explicit wait uses .WebDriverWait() function and implicit wait uses .implicitly_wait() function
#3.1 difference: you may want to use an additional variable (like driver_wait) to the elements to apply explicit waits

driver.implicitly_wait(10)
driver_wait = WebDriverWait(driver,10)

#---- click the button to start loading the element to appear , time to load will vary
button = driver.find_element(By.CSS_SELECTOR,'#input-example > button')
button.click()

#4 difference: explicit wait uses .until() and implicit waits uses .find_element()
#5 difference: explicit wait needs an explicit condition to be present (like to be clickable)
#6 difference: explicit wait needs a (tupple) when two or more arguments are passed to the expected condition method !

#------- using Implicit Wait will fail !
#textBox = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]') # IMPLICIT WAIT
textBox = driver_wait.until(expected_conditions.element_to_be_clickable( (By.CSS_SELECTOR, '#input-example > input[type=text]') ) ) #EXPLICIT WAIT

#----- If correct wait is used, the text is typed into the textbox and test will pass, otherwise it will fail
textBox.send_keys('Correct Wait')

driver.quit()
