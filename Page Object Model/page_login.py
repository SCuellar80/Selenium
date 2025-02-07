#Import Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self, driver):
        # tip using temporaly self.driver = webdriver.Chrome()
        # will show you the methods when you type self.driver.<here the methods will appear>
        #self.driver = webdriver.Chrome()
        self.driver = driver
        self.url = 'https://the-internet.herokuapp.com/login'
        self.username_textbox = (By.ID,'username')
        self.password_textbox = (By.ID, 'password')
        self.login_button = (By.CSS_SELECTOR,'#login > button')
        self.login_text = (By.ID,'flash') #this element's text will contain the status of the login

    def open_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login_result(self):
        return self.driver.find_element(*self.login_text).text
