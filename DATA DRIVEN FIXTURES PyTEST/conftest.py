import pytest
@pytest.fixture(scope="class")
def dataload():
    print("User profile data is being created")
    return ["Vansh","Ahuja","vanshahuja266@gmail.com"]
