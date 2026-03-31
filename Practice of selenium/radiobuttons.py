from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver .get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)

time.sleep(2)
radiobuttons = driver.find_elements(By.XPATH,"//input[@class='radioButton']")
print(len(radiobuttons))
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        time.sleep(2)
        assert radiobutton.is_selected()