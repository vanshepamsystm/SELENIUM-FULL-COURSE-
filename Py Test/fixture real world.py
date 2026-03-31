import pytest

@pytest.fixture
def browser():
    print("Open Browser")
    yield
    print("Close Browser")
@pytest.fixture
def login():
    print("Login User")
    yield
    print("Logout User")
def test_fixture(browser,login):
    print("test running")