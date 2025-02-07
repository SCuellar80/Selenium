from selenium import webdriver
import pytest #this runs with pytest installed
from page_login import LoginPage

def test_login():
    loginPage = LoginPage(webdriver.Chrome())
    loginPage.open_page()
    loginPage.enter_username('tomsmith')
    loginPage.enter_password('SuperSecretPassword!')
    loginPage.click_login()
    result = loginPage.login_result()
    assert result == "You logged into a secure area!\n×"

