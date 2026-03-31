from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.username_input = (By.ID,"username")
        self.password_input = (By.ID, "password")
        self.terms_button = (By.CSS_SELECTOR, "#terms")
        self.sign_button = (By.CSS_SELECTOR, "#signInBtn")


    def login(self):
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password_input).send_keys("Learning@830$3mK2")
        self.driver.find_element(*self.terms_button).click()
        self.driver.find_element(*self.sign_button).click()

