from selenium.webdriver.common.by import By

class ShopPage:
    def __init__(self,driver):
        self.driver = driver
        self.add_to_cart = (By.XPATH, "//app-card-list//app-card[1]//div//div[2]//button")
        self.click_checkout=  (By.CSS_SELECTOR, "div[id='navbarResponsive'] a")
    def shop(self):
        self.driver.find_element(*self.add_to_cart).click()
        self.driver.find_element(*self.click_checkout).click()

    def addToCart(self, param):
        pass