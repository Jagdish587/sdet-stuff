import pytest

def test_addition():
    assert 1 + 1 == 2



def divide_numbers(numerator, denominator):
    return numerator / denominator

def test_divide_numbers():
    # divide_numbers(10, 0)
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

