import pytest

@pytest.fixture()
def method1():
    print("Opening Google Through Selenium")
    yield
    print("Automation Done")
@pytest.fixture()
def method2():
    print("You tube got typed on google and clicked")
    yield
    print("Closing Google")
def test_method(method2,method1):
    print("Playing Songs on You Tube")