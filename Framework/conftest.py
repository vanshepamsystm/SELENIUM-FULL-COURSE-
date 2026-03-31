from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store", default = "Chrome", help="browser selection"
    )
#edefault - chrome means if we don't specify any browser option so as a backup option it will run in chrome and if u specify it in cmd then it will override the default value
# above things is mandatory to run

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name=="Chrome":
        driver = webdriver.Chrome()
    elif browser_name=="Firefox":
        driver = webdriver.Firefox()
    elif browser_name=="edge":
        driver = webdriver.Edge()

    driver.implicitly_wait(4)
    yield driver
    driver.quit()
