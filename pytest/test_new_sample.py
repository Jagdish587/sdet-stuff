import pytest

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    print("request.function = ", request.function)
    print("request.param = ", request.param)
    return request.param


def test_browser(browser):
    print("browser = ", browser)