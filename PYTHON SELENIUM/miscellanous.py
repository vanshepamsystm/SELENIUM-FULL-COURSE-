from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument('headless')

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") # to go at bottom
driver.get_screenshot_as_file("screeen.png")

