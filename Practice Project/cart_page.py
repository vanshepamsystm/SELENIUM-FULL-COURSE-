from selenium.webdriver.common.by import By
from BasePage import *

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_name = (By.XPATH, "//div[@class='inventory_item_name']")

    def get_cart_item_name(self):
        return self.get_text(self.product_name)