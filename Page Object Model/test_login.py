from selenium import webdriver
import pytest
#from Pages.login_page import LoginPage
from page_login import LoginPage

def test_login(driver):
    loginPage = LoginPage(driver)
    loginPage.open_page()
    loginPage.enter_username('tomsmith')
    loginPage.enter_password('SuperSecretPassword!')
    loginPage.click_login()

chrome_driver = webdriver.Chrome()
test_login(chrome_driver)
chrome_driver.quit()