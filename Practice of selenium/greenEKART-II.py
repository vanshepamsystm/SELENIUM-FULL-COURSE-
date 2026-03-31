from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(7)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("Lo")
buttons = driver.find_elements(By.CSS_SELECTOR,"div[class='product'] div .increment")
for button in buttons:
    button.click()
cart = driver.find_elements(By.CSS_SELECTOR,"div[class='product'] div button")
for button in cart:
    button.click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(3)
products = driver.find_elements(By.CSS_SELECTOR,".product-name")
actual_list = []
for product in products:
    actual_list.append(product.text)
expected_list = ['Cauliflower - 1 Kg', 'Musk Melon - 1 Kg', 'Water Melon - 1 Kg']
print(actual_list)
assert actual_list == expected_list
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("vansh")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
time.sleep(7)
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
time.sleep(2)
amount = driver.find_element(By.CSS_SELECTOR,".totAmt").text
amount = float(amount)
print(amount)
discount = driver.find_element(By.CSS_SELECTOR,".discountAmt").text
discount = float(discount)
print(discount)
assert amount > discount
