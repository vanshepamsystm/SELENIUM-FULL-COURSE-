import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(results))
for result in results:
    result.find_element(By.XPATH,"div/button").click()
#extract product names here
names = driver.find_elements(By.CSS_SELECTOR,"div[class='product'] h4")
#making list to add product names
actual_list = []
#using loop for all product names to add in list using append
for name in names:
    actual_list.append(name.text)
print("Actual list using Script: ",actual_list)
#created expected list
expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
#checking validations
assert actual_list == expected_list
driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#SUM VALIDATION
# prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
Sum = 0
for price in prices:
    Sum = Sum + int(price.text)
print(Sum)
total = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert Sum == total
# time.sleep(2) #- if i dont use it will throw error after checkout we are immediately entering code but it didnt apppear by the time,but when we use implict here it will work
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,13)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
#checking validation that discounted amount is less than original
discountedAmount = driver.find_element(By.CSS_SELECTOR,".discountAmt")
print(float(discountedAmount.text))
assert float(discountedAmount.text) < Sum

