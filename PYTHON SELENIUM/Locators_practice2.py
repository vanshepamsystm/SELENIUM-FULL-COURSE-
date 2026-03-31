from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("file:///C:/Users/VanshAhuja/Desktop/practice2.html")

driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Vansh")
driver.find_element(By.XPATH,"(//input[@type = 'text'])[2]").send_keys("9588199226")
driver.find_element(By.CSS_SELECTOR,"input[value='Male']").click()
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

mssg = driver.find_element(By.ID,"message").text
print(driver.title)
print(driver.current_url)
print(mssg)
time.sleep(5)

