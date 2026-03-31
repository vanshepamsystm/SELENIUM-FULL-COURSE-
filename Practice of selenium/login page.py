from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Learning@830$3mK2")
time.sleep(2)
dropdown = Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
dropdown.select_by_visible_text("Teacher")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)
