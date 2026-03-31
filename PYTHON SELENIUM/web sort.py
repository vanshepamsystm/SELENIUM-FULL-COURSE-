import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
    
# options = Options()
# options.add_argument("headless")

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
time.sleep(2)
elements = driver.find_elements(By.XPATH,"//tr//td[1]")
browser_sorted_list = []
for element in elements:
    browser_sorted_list.append(element.text)

original_list = browser_sorted_list.copy()
browser_sorted_list.sort()

assert browser_sorted_list == original_list

