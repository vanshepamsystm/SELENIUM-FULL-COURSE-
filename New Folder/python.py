import json
import pytest
path = "C:\\Users\\VanshAhuja\\PycharmProjects\\PythonTesting\\New Folder\\file.json"
with open(path) as f:
    test_data = json.load(f)
    test_list = test_data['data']

@pytest.mark.parametrize("data",test_list)
def test_login(data):
    print(data['username'])