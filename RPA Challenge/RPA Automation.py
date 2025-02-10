from selenium import webdriver
from selenium.webdriver.common.by import By
from page_excel import ExcelReader

driver = webdriver.Chrome()
driver.get("https://rpachallenge.com/")
start = driver.find_element(By.CSS_SELECTOR, "button[class*='btn-large']")
start.click()

excel_reader = ExcelReader()
excel_data = excel_reader.read_excel_data()
columnsText = excel_data.pop(0)
columnsText = [
    "input[ng-reflect-name='labelFirstName']",
    "input[ng-reflect-name='labelLastName']",
    "input[ng-reflect-name='labelCompanyName']",
    "input[ng-reflect-name='labelRole']",
    "input[ng-reflect-name='labelAddress']",
    "input[ng-reflect-name='labelEmail']",
    "input[ng-reflect-name='labelPhone']"
]
for row in excel_data:
        for column in range(len(columnsText)):
            label = driver.find_element(By.CSS_SELECTOR, columnsText[column])
            label.send_keys(row[column])
        # After all fields completed, submit it
        button = driver.find_element(By.CSS_SELECTOR, "input[value*='Submit']")
        button.click()

time = driver.find_element(By.CSS_SELECTOR, "div[class*='message2']")
timeText = time.text
print(timeText)

driver.quit()
