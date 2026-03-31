from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class checkout_Confirmation:
    def __init__(self,driver):
        self.driver=driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country  = (By.ID, "country")
        self.text = (By.CSS_SELECTOR, ".alert")

    def checkout_page(self):
        self.driver.find_element(*self.checkout_button).click()


    def address_page(self):
        self.driver.find_element(*self.country).send_keys("Ind")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div//ul//li//a[text()='India']")))

        self.driver.find_element(By.XPATH, "//div//ul//li//a[text()='India']").click()
        self.driver.find_element(By.XPATH, "//div//label[@for='checkbox2']").click()
        self.driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()


    def validate_mssg(self):
        mssg = self.driver.find_element(*self.text).text
        assert "Success! Thank you!" in mssg