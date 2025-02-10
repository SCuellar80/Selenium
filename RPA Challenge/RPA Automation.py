from selenium import webdriver
from selenium.webdriver.common.by import By
from page_excel import ExcelReader
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument("--headless")  # enable headless, comment it to disable it
firefox_options.add_argument("--disable-gpu")  # Disables GPU (recommended for headless)
driver = webdriver.Firefox(firefox_options)
driver.get("https://rpachallenge.com/")
start = driver.find_element(By.CSS_SELECTOR, "button[class*='btn-large']")
start.click()

excel_reader = ExcelReader()
excel_data = excel_reader.read_excel_data()

button = driver.find_element(By.CSS_SELECTOR, "input[value*='Submit']")

for row in excel_data:

    labelFirstName = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")
    labelLastName = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")
    labelCompanyName = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")
    labelRole = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")
    labelAddress = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")
    labelEmail = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")
    labelPhone = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")

    labelFirstName.send_keys(row[0])
    labelLastName.send_keys(row[1])
    labelCompanyName.send_keys(row[2])
    labelRole.send_keys(row[3])
    labelAddress.send_keys(row[4])
    labelEmail.send_keys(row[5])
    labelPhone.send_keys(row[6])

    # After all fields completed, submit it
    button.click()

time = driver.find_element(By.CSS_SELECTOR, "div[class*='message2']")
timeText = time.text
print(timeText)

driver.quit()
