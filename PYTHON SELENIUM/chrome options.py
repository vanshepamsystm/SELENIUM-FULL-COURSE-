from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore--certificate-errors")
#to access dangerous site

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://google.com")

print(driver.title)
