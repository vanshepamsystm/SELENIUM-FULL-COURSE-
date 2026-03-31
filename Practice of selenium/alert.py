import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)
name = "Vansh"
driver.find_element(By.NAME,"enter-name").send_keys(name)
time.sleep(2)
driver.find_element(By.ID,"alertbtn").click()
time.sleep(2)
#feature
alert = driver.switch_to.alert #cannot read direclty we have to switch to alert mode
assert "Vansh" in alert.text   #using assert to check a test case
print(alert.text)
alert.accept()   #positive
time.sleep(2)
# alert.dismiss()  #negative


# this is how to handle browser based alerts