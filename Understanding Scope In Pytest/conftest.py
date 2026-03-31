import pytest

@pytest.fixture(scope="module")
def browser():
    print("Opening Browser")
    yield
    print("Closing Browser")