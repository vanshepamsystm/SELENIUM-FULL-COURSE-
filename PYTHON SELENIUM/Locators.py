import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/Users/VanshAhuja/Desktop/form.html")


# locators selenium support - ID, Xpath, CSSselector, Classname, name, Text


driver.find_element(By.NAME,"username").send_keys("VanshAhuja10")
time.sleep(2)
driver.find_element(By.ID,"email").send_keys("vanshahuja266@gmail.com")
time.sleep(2)
driver.find_element(By.ID,"phone").send_keys("9588199226")
time.sleep(2)
driver.find_element(By.NAME,"usercity").send_keys("Sonipat")
driver.find_element(By.ID,"male").click()
driver.find_element(By.ID,"python").click()
# driver.find_element(By.ID,"submitBtn").click()

driver.find_element(By.XPATH,"//button[@id = 'submitBtn']").click()
time.sleep(2)

