import pytest
@pytest.fixture(params=["Chrome","Firefox"])
def cross_browser(request):
    return request.param