from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rpachallenge.com/")

start = driver.find_element(By.CSS_SELECTOR,"button[class*='btn-large']")
start.click()

for _ in range(10):
    label = driver.find_element(By.XPATH, "//label[text()='Role in Company']")
    input_element = label.find_element(By.XPATH, "./following-sibling::input")
    input_element.send_keys("QA Manager")
    button = driver.find_element(By.CSS_SELECTOR,"input[value*='Submit']")
    buttonText = button.get_attribute("value")
    button.click()
    print(buttonText)

time = driver.find_element(By.CSS_SELECTOR,"div[class*='message2']")
timeText = time.text
print(timeText)

driver.quit()