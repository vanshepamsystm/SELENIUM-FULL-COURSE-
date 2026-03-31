import pytest

@pytest.fixture(scope="module")   #here scope="class"   means below fixture runs only once in whole not for every test case
def browser():
    print("Opening Browser")
    yield
    print("Closing Browser")