from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")

driver.find_element(By.XPATH,"//a[text()='Dynamic Content']").click()

#  Store element
# heading = driver.find_element(By.XPATH,"//h3[text()='Dynamic Content']")

heading = driver.find_element(By.XPATH,"//h3[text()='Dynamic Content']")
# Now refresh
driver.refresh()
#  Use old reference
try:
    print(heading.text)   # This will throw StaleElementReferenceException
except StaleElementReferenceException:
    print("element became stale. Re-locating")
    heading = driver.find_element(By.XPATH, "//h3[text()='Dynamic Content']")
    print(heading.text)