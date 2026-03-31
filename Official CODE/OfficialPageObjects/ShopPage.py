from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self,driver):
        self.driver=driver
        self.products = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.XPATH,"//a[@class='nav-link btn btn-primary']")

    def add_to_cart(self,product_name):
        products = self.driver.find_elements(*self.products)
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()

    def go_to_cart(self):
        self.driver.find_element(*self.checkout_button).click()