from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.username = (By.CSS_SELECTOR, "#username")
        self.password = (By.CSS_SELECTOR, "#password")
        self.terms = (By.NAME, "terms")
        self.signbutton = (By.ID, "signInBtn")

    def login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.terms).click()
        self.driver.find_element(*self.signbutton).click()
