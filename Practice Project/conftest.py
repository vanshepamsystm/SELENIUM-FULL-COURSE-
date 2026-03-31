import pytest
import pytest_html
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="edge",
        help="browser selection"
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser:{browser_name}")
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(2)
    yield driver
    driver.quit()


import pytest
import pytest
import os
from pytest_html import extras  # Critical import for the report attachment


# 1. Separate function for capturing the screenshot
def _capture_screenshot(driver, name):
    folder = "screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Clean the name to avoid OS path errors
    clean_name = name.replace("/", "_").replace("\\", "_").replace(":", "_")
    file_path = os.path.join(folder, f"{clean_name}.png")

    driver.save_screenshot(file_path)
    # We return the relative path so the HTML report can find it
    return f"screenshots/{clean_name}.png"


# 2. The Hook to catch failure and attach to report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Create the 'extra' list if it doesn't exist
    extra = getattr(report, "extra", [])

    # Only trigger on the 'call' phase (the actual test execution)
    if report.when == "call":
        # Check if the test failed
        if report.failed:
            # 3. Retrieve the driver
            # Change "driver" if your fixture is named "setup" or "browser"
            driver = item.funcargs.get("driver")

            if driver:
                test_name = item.name
                screenshot_path = _capture_screenshot(driver, test_name)

                # 4. Correct way to attach to pytest-html
                # We use the 'extras' module we imported at the top
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screenshot_path
                extra.append(extras.html(html))

            report.extra = extra