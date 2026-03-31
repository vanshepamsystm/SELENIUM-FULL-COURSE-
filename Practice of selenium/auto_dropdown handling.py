from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
time.sleep(2)
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
time.sleep(2)
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        time.sleep(2)
        break
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"