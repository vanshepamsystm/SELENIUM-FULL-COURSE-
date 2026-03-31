import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.switch_to.frame("courses-iframe")

driver.find_element(By.XPATH,"//a[text()='Courses']").click()
time.sleep(5)

#getting back to main window default where we initialized like from where we started
driver.switch_to.default_content()
print(driver.find_element(By.XPATH,"//fh1[(text()='Practice Page')]").text)