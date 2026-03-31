# import pytest
#@pytest.mark.usefixtures("cross_browser") -. we dont use this marker here because fixture is returning data , we only use this marker when fixture dont return data
#If a fixture returns data (using return or yield), you cannot use @pytest.mark.usefixtures.
def test_cross_browser(cross_browser):
    print(cross_browser)