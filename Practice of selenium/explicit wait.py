import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
# time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
# time.sleep(2)
# print(len(results))
for result in results:
    result.find_element(By.XPATH,"div/button").click()
    # time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
# time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()#imp
# time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
# time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
# time.sleep(5)
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
# time.sleep(3)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
# time.sleep(2)