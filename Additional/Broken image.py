from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.google.com/")

images = driver.find_elements(By.TAG_NAME, "img")

broken_images = []

for image in images:
    src = image.get_attribute("src")

    # Skip if no src
    if src:
        width = driver.execute_script(
            "return arguments[0].naturalWidth;", image
        )

        if width == 0:
            broken_images.append(src)

print("Broken Images:", broken_images)