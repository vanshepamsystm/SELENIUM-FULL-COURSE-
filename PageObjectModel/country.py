from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class FinalPage:
    def __init__(self,driver):
        self.driver=driver
        self.search_country = (By.CSS_SELECTOR, "#country")
        self.click_country = (By.LINK_TEXT, "India")
        self.terms_condition = (By.CSS_SELECTOR, "input[id='checkbox2']")
        self.purchase_button = (By.XPATH, "//input[@type='submit']")
        self.print_text = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    def Lastpage(self):
        self.driver.find_element(*self.search_country).send_keys("Ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.click_country))
        self.driver.find_element(*self.click_country).click()
        self.driver.find_element(*self.terms_condition).send_keys(Keys.ENTER)
        self.driver.find_element(*self.purchase_button).click()
        mssg = self.driver.find_element(*self.print_text).text

        assert "Success! Thank you!" in mssg