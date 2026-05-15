import pytest

"""
In pytest, the request object is a special built-in fixture that gives you access to:

the current test context
fixture metadata
test class instance
parametrization data
markers
config
module/class/function info

It’s one of the most powerful advanced pytest features.


| Attribute                | Meaning                |
| ------------------------ | ---------------------- |
| `request.node`           | current test node      |
| `request.module`         | current module         |
| `request.cls`            | current test class     |
| `request.function`       | current test function  |
| `request.config`         | pytest config          |
| `request.param`          | parametrized value     |
| `request.fixturenames`   | all fixture names used |
| `request.addfinalizer()` | teardown registration  |


"""

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    print("request.function = ", request.function)
    print("request.param = ", request.param)
    return request.param


def test_browser(browser):
    print(browser)