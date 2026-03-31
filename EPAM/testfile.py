import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.maximize_window()
driver.get("https://www.epam.com/")
wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#onetrust-accept-btn-handler"))).click()

driver.find_element(By.XPATH,"//ul//li[5]//span//a[text()='Careers']").click()

driver.find_element(By.XPATH,"//div//div//div//a[@class='button-body']//div//span[text()='Start Your Search Here']").click()

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#onetrust-accept-btn-handler"))).click()

driver.find_element(By.NAME,"search").send_keys("Python")

driver.find_element(By.XPATH,"//div[@class='Dropdown_defaultOption__pvL_3 ym-disable-keys dropdown__indicators css-1wy0on6']//div").click()

driver.find_element(By.XPATH,"//label[@class='Checkbox_label__DlX3A Checkbox_large__vMLp7 Checkbox_light__lYB6G']//span[text()='Remote']").click()


driver.find_element(By.NAME,"submit_search_box_button").click()

time.sleep(2)

wait.until(EC.element_to_be_clickable((
    By.XPATH,
    "//div[@class='List_list___59gh']//div[@class='JobCard_panel__gTD7e'][1]//div//div//div"
))).click()


extracted_text = driver.find_element(By.XPATH,"//div//h1[text()='Python Developer']").text

assert 'Python' in extracted_text
