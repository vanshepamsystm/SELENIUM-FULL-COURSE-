# from selenium.webdriver.common.by import By
# from BasePage import *
#
# class InventoryPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#         self.product = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
#         self.cart_button = (By.ID, "shopping_cart_container")
#         self.page_title = (By.XPATH, "//span[@class='title']")
#
#     def add_product_to_cart(self):
#         self.click(*self.product).click()
#
#     def open_cart(self):
#         self.click(*self.cart_button).click()
#
#     def get_page_title(self):
#         return self.get_text(*self.page_title)


from selenium.webdriver.common.by import By
from BasePage import *

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.product = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
        self.cart_button = (By.ID, "shopping_cart_container")
        self.page_title = (By.XPATH, "//span[@class='title']")

    def add_product_to_cart(self):
        self.click(self.product)

    def open_cart(self):
        self.click(self.cart_button)

    def get_page_title(self):
        return self.get_text(self.page_title)