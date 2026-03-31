from selenium.webdriver.common.by import By
from BasePage import *


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_click = (By.ID, "login-button")

    def login(self, username, password):
        self.send_keys(self.username, username)
        self.send_keys(self.password, password)
        self.click(self.login_click)