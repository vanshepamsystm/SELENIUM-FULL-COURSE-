import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

#login page
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("Learning@830$3mK2")
driver.find_element(By.NAME,"terms").click()
driver.find_element(By.ID,"signInBtn").click()




#selecting products adding if product we want is there and add to cart
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()   #go to cart script



#checkout page
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()


#add location
driver.find_element(By.ID,"country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div//ul//li//a[text()='India']")))
driver.find_element(By.XPATH,"//div//ul//li//a[text()='India']").click()

driver.find_element(By.XPATH,"//div//label[@for='checkbox2']").click()

driver.find_element(By.XPATH,"//input[@class='btn btn-success btn-lg']").click()


mssg = driver.find_element(By.CSS_SELECTOR,".alert").text


assert "Success! Thank you!" in mssg