# import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH,"//a[text()='Shop']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"/z'iphone X']").click()
# time.sleep(2)
driver.find_element(By.XPATH,"//app-card-list//app-card[1]//div//div[2]//button").click()
# time.sleep(5)

driver.find_element(By.CSS_SELECTOR,"div[id='navbarResponsive'] a").click()
# time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()
# time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#country").send_keys("Ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,"input[id='checkbox2']").send_keys(Keys.ENTER)
# time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
# time.sleep(3)
mssg = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text

assert "Success! Thank you!" in mssg
# time.sleep(2)