from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)
driver.get("https://accounts.google.com/ServiceLogin?hl=es&service=mail")
email = driver.find_element(By.ID,"identifierId")
email.click()
email.send_keys("armando7godinez@GMAIL.COM")
siguiente = driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span')
siguiente.click()
passw = driver.find_element(By.NAME, "Passwd")
passw.send_keys("ElPassWor")
siguiente = driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span')
siguiente.click()
print(driver.title)  # Verifica que funciona
