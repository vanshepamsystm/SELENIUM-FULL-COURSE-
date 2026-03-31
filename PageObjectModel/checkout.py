from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self,driver):
        self.driver=driver
        self.click_checkout_button = (By.CSS_SELECTOR, ".btn.btn-success")

    def Checkout(self):
        self.driver.find_element(*self.click_checkout_button).click()