import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

element = driver.find_element(By.CSS_SELECTOR,"#mousehover")
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(5)
action = ActionChains(driver)
action.move_to_element(element).perform()
# driver.find_element(By.XPATH,"//a[text()='Reload']")
action.click(driver.find_element(By.XPATH,"//a[text()='Reload']")).perform()