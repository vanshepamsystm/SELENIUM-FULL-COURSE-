import pytest

@pytest.mark.parametrize("data",[
{"name":"vansh","age":32},
{"name":"sid","age":21}
])
def test_login(data):
    print(data['name'],data['age'])