import pytest
@pytest.fixture()
def browser():
    print("open browser")
    yield
    print("close browser")
@pytest.fixture()
def login():
    print("login")
    yield
    print("logout")