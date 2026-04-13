import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (1, 1, 2),
    (4, 5, 9)
])
def test_add(a, b, expected):
    assert a + b == expected